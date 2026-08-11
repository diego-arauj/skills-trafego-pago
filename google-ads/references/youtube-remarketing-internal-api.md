# Públicos de YouTube (view de vídeo) — endpoint INTERNO do painel

## O problema
A **API oficial do Google Ads NÃO cria nem edita públicos de "usuários do YouTube"** (viu vídeo, viu vídeo específico, inscritos, etc.). Confirmado no fórum oficial da API: *"the Google Ads API does not support the programmatic creation of YouTube user segments"*. O `create.py`/`update.py` desta skill também não cobrem isso. Pela API oficial (GAQL `user_list`) dá só pra **ler** essas listas.

## A solução (engenharia reversa do painel)
O painel de públicos usa **endpoints RPC internos** (mesma origem, autenticados por cookie de sessão). Dá pra replicá-los. Base:

```
https://ads.google.com/aw_displayads/audiencecenter/_/rpc/<Service>/<Method>
```

| Service/Method | O que faz |
|---|---|
| `VideoRemarketingService/Create` | Cria lista de view de vídeo |
| `VideoRemarketingService/Update` | Edita a lista (SUBSTITUI a lista de vídeos inteira) |
| `VideoRemarketingService/Get` | Lê a lista (com títulos dos vídeos) |
| `VideoSearchService/Search` | Resolve um vídeo (URL/ID → metadados) dentro de um canal |
| `UserListService/List`, `AudienceService/List` | Listagens |

### Método HTTP
- `POST`, `content-type: application/x-www-form-urlencoded;charset=UTF-8`
- Query: `?authuser=0&xt=awn&acx-v-bv=<build>&acx-v-clt=<ts>&rpcTrackingId=<Service>.<Method>:1&f.sid=<sid>`
- Corpo (form): `hl=pt_BR&__lu=<uid>&__u=<uid2>&__c=<cid>&f.sid=<sid>&ps=aw&__ar=<PAYLOAD JSON url-encoded>&drapt=<token>&activityContext=...&activityType=SAVE&activityId=<rand>&uniqueFingerprint=<sid>_<rand>_1&previousPlace=/aw/audiences/management&activityName=...&destinationPlace=...`
- O que importa de verdade é o **`__ar`** (payload) + a **autenticação** (abaixo). O resto (`activity*`, `f.sid`) é telemetria/rastreio.

### Payloads (`__ar`, JSON) — atenção: numeração dos campos MUDA entre Create e Update
**Create** — `{"1":11,"2":<channelId>,"3":[videoIds],"4":<nome>,"5":"<dias>","6":true,"7":<ocid>,"11":false,"12":false}`
**Update** — `{"1":<listId>,"2":11,"3":[videoIds],"4":<nome>,"5":"<dias>","6":1,"7":<ocid>,"8":<channelId>,"10":"","11":false}`
**Get** — `{"1":<listId>,"2":<ocid>}`
**Search** — `{"1":<channelId>,"2":"<video URL>","3":{"1":0,"2":100},"4":<ocid>}`

Campos: `1`=tipo (11 = "viu vídeos específicos") ou o listId no Update; `channelId`=canal do YouTube VINCULADO à conta (ex.: `UC...`); `3`=array de videoIds; `5`=duração da associação em dias (máx **540**). Resposta de sucesso: `{"1":{"1":<listId>,...,"4":[videoIds],"5":<nome>,"6":"<dias>"}}`.

### ⚠️ Limite: 40 vídeos por lista
`VideoRemarketingService/Create`/`Update` aceita no **máximo ~40 vídeos** por lista. Acima disso a resposta é o erro `{"2":[7]}` (código 7 = excedeu). Pra cobrir mais que 40: quebrar em várias listas e somar no ad group, OU usar janela rolante (manter só os 40 mais recentes e sobrescrever via Update).

### Autenticação (o ponto crítico)
- **Cookies de sessão** do navegador logado — NÃO vêm no HAR (o Chrome remove). Só existem dentro do navegador logado.
- **Header `x-framework-xsrf-token`** — obrigatório. **Gira a cada sessão/carregamento de página** (não dá pra fixar).
- **Header `x-same-domain: 1`**.
- **`drapt`** (no corpo) — token anti-forgery. **Estável por usuário/app** (reaproveitável por bastante tempo; se um dia quebrar, recapturar).
- **`f.sid`** — id de sessão gerado no cliente; pode ser um número aleatório novo a cada chamada.
- A **API oficial (OAuth)** desta skill NÃO autentica esse endpoint — é outro sistema (cookie de sessão web).

## Como executar
1. **Manual/pontual:** rodar no **console do Chrome logado** (mesma origem `ads.google.com`), `fetch(..., {credentials:"include", headers:{"x-framework-xsrf-token":XSRF,"x-same-domain":"1"}})`. Os cookies vão sozinhos; o xsrf tem que ser da sessão atual.
2. **Automático (job local):** Playwright abrindo o **profile do Chrome logado**, capturar o `x-framework-xsrf-token` fresco por **intercept de rede** (a página dispara RPCs sozinha), e então disparar os Updates. É o único jeito realmente "liga e esquece", porque o xsrf gira. Não dá pra rodar num servidor sem navegador logado.
3. Enumerar vídeos de playlist/canal: pelo lado de fora (yt-dlp / YouTube), NUNCA de dentro do painel (CORS bloqueia YouTube a partir de `ads.google.com`).

## Como recapturar (quando algo mudar)
Painel → Gerenciador de públicos → criar/editar um público de YouTube com o DevTools → Network (Preserve log) gravando → "Save all as HAR with content". O HAR traz URL + payload (`__ar`) + `drapt`/`xsrf` nos headers (mas **não** os cookies). Decodificar o `__ar` (url-decode + JSON).

## Automação recorrente — recipe TESTADO (o que funciona de verdade)
Rodando em produção como job semanal (Playwright + yt-dlp + LaunchAgent no macOS), mantendo uma janela rolante dos vídeos mais recentes de uma playlist em 8 durações de lista. Macetes que custaram horas pra descobrir:

- **`drapt` só aparece quando se ABRE um segmento.** Na tela de LISTA de segmentos, o load traz o `x-framework-xsrf-token` (no header de qualquer RPC) mas **não** o `drapt`. O `drapt` só vem no corpo de uma RPC de ação — ex.: clicar num público dispara `VideoRemarketingService/Get` com `drapt`. Pra capturar ao vivo: depois do load, clicar num público pelo nome (`page.get_by_text("[YT]...", exact=True).click()`).
- **`drapt` é estável por usuário** → serve um valor fixo como **fallback** se a captura ao vivo falhar. Só recapturar se um dia TODOS os updates derem erro de token.
- **`xsrf` gira a cada sessão** → capturar fresco sempre (header de qualquer RPC no load). Nunca fixar.
- **Profile dedicado, não o do dia a dia.** Playwright `launch_persistent_context` num user-data-dir só da automação (ex.: `~/.gads-automation-profile`), logado 1x (`--setup`). Assim não conflita (lock do SingletonLock) com o Chrome que o usuário usa.
- **Headless funciona** com o profile já logado (cookies persistem no dir) — o LaunchAgent roda invisível e dá 8/8.
- **Pegadinha do Playwright:** ao passar um dict pro `page.evaluate`, as CHAVES têm que ser **string**. Dict com chave int (`{7:"id"}`) → erro `expected string, got number`. Converter: `{str(k):v for k,v in d.items()}`.
- **Enumerar a playlist:** `yt-dlp --flat-playlist --playlist-end 40 --print "%(id)s"` (ordem newest-first). Deslogado, playlist entrega no máx ~100 itens (resto é privado/members, não segmentável).
- **CORS:** não dá pra buscar YouTube de dentro de `ads.google.com` (o job pega os vídeos por fora, com yt-dlp, e só dispara os Updates dentro do painel).
- **Alerta de falha local (sem depender de permissão):** `osascript -e 'display dialog ... giving up after N'` (janela, impossível de perder) + `afplay /System/Library/Sounds/*.aiff` (som). O banner (`display notification`) depende de permissão de Notificações do "Editor de Scripts" — pode não aparecer.
- **Fallback manual (sem Playwright):** snippet no console que faz *monkeypatch* de `fetch` e `XMLHttpRequest` pra capturar o token fresco da própria página (precisa 1 clique num público pra disparar a RPC com `drapt`), e então dispara os 8 Updates. Bom pra rodar na mão quando não quiser o job.

## Segurança
NUNCA commitar valores de cookies, `xsrf` ou `drapt` em documento nenhum — são credenciais de sessão, equivalem à sua senha do painel. Aqui ficam só nomes de campo e esquemas. O `drapt` estável (o fallback) pode ficar **apenas no script local da automação**, na sua máquina, nunca em arquivo versionado ou compartilhado. IDs de conta (ocid), de canal e de lista não são segredo.

## O que você precisa levantar antes de reproduzir
- **customer id** e **ocid** da conta (o `ocid` aparece na própria URL do painel, `?ocid=...`).
- **channel id** do canal do YouTube **vinculado à conta** (formato `UC...`). Público de view de vídeo só funciona com canal vinculado.
- **playlist ou lista de vídeos** que vai alimentar o público, enumerada por fora com `yt-dlp`.
- O profile do Chrome logado na conta certa (se você opera vários clientes, é o profile daquele cliente).

**Aviso:** isto é engenharia reversa de endpoint interno, não API pública. Pode mudar sem avisar e não tem suporte do Google. Use para automatizar o que você já faria na mão no painel, e mantenha o caminho manual como plano B.
