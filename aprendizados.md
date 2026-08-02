# Erros e acertos ao subir campanhas pela API

Cada entrada aqui custou tempo, dinheiro ou uma campanha rodando errada. O Claude **deve ler
este arquivo antes de criar qualquer objeto** na conta.

Todos os IDs foram substituídos por placeholders. Onde aparece `act_XXX`, `<PAGE_ID>`,
`<IG_ID>`, `<PIXEL_ID>` ou `<VIDEO_ID>`, use os valores da conta em que estiver trabalhando.

As datas indicam quando o comportamento foi observado. A API da Meta muda: entrada antiga que
contradiz entrada nova perde para a nova, e isso está sinalizado no texto.

Formato para novas entradas:

```
### AAAA-MM-DD — título curto
**Regra:** o que fazer ou nunca fazer.
**Como aplicar:** o passo prático.
**Contexto:** o que aconteceu para gerar o aprendizado (sem nome de cliente).
```

---

## REGRA Nº 1 — Pré-voo obrigatório antes de ativar qualquer anúncio

Criativo montado do zero pela API sai **sem alguns campos, e a API não reclama**. Ela aceita,
cria, o anúncio entrega, e só o resultado ruim denuncia semanas depois.

Os quatro campos que somem em silêncio:

| Campo | Onde fica | O que quebra sem ele |
|---|---|---|
| `page_welcome_message` | `object_story_spec.video_data` ou `link_data` | Em clique para WhatsApp, é a mensagem que já vem digitada para o lead. Sem ela o lead abre o WhatsApp com a caixa vazia e tem que inventar o que escrever. Boa parte desiste. |
| `url_tags` | raiz do criativo | UTMs. Sem elas o CRM perde a atribuição por anúncio. |
| `message` | dentro de `video_data` / `link_data` | O anúncio roda **sem uma linha de texto**. |
| `title` | idem | Cai no default da Meta ("Converse conosco"). |

**Procedimento, em toda conta e toda campanha:**

1. Antes de criar, leia um criativo **já publicado e performando** da mesma conta e copie os
   campos literalmente. Cada conta tem seu próprio modelo de mensagem de boas-vindas (um JSON
   grande com `template_id`). **Nunca remontar esse JSON na mão.**
2. Crie o criativo novo com os campos copiados.
3. **Releia o criativo criado antes de ativar.** Se qualquer um dos quatro vier vazio, **aborte
   a ativação** e avise o operador. Não ativar "para não perder tempo".

**Quanto isso custa quando falha (dois casos reais, mesma conta):**

- Três criativos subiram sem `page_welcome_message` num teste de gancho. Dentro da mesma campanha
  e do mesmo público, o anúncio que tinha a mensagem fez custo por lead de R$ 8,25; os três sem
  ela fizeram R$ 15,10, R$ 19,60 e R$ 45,70. O teste inteiro rodou viciado e o custo alto foi
  lido como "criativo ruim".
- Três anúncios flexíveis rodaram com `message` de zero caractere. A campanha gastou quase
  R$ 2.000 em duas semanas assim, e a conclusão "formato flexível não funciona nesta conta" saiu
  de um teste que nunca teve texto.

### 2026-07-27 — Ler o criativo sem campo aninhado devolve spec TRUNCADO (falso "campo ausente")

**Regra:** em criativo flexível (`contextual_multi_ads`) e em criativo feito a partir de post
existente, `GET /<creative>?fields=object_story_spec` volta só com `page_id` e
`instagram_user_id`, sem `video_data`/`link_data`. Parece que os campos não foram gravados.
**Não foram perdidos: a leitura é que é rasa.**

Peça aninhado:

```
GET /<creative_id>?fields=object_story_spec{video_data{video_id,title,message,call_to_action,page_welcome_message,image_url}}
```

**Como aplicar:** o pré-voo acima **só vale com leitura aninhada**. Com leitura rasa o resultado
é sempre "ausente", e o risco é duplo: abortar uma ativação boa, ou "corrigir" um criativo que
já estava certo.

---

## Criativos

### 2026-07-27 — Criativo de post existente se recria por `object_story_id`, não por `object_story_spec`

**Regra:** num criativo montado a partir de post já existente, o `object_story_spec` volta da API
sem `link_data`/`video_data`. Tentar criar um criativo novo com esse spec truncado devolve
**`(#3) Application does not have the capability to make this API call`**, que **parece problema
de permissão do app e não é**: é payload incompleto.

**Como aplicar:** antes de recriar um criativo, veja se o `object_story_spec` tem conteúdo de
story. Se não tiver e existir `effective_object_story_id`, referencie o post:

```
POST act_XXX/adcreatives
  object_story_id: "<effective_object_story_id do criativo antigo>"
  url_tags: "<utms>"
```

Bônus: reusar o post original **preserva curtidas e comentários** (prova social).

Dois detalhes: a Meta **deduplica** criativos idênticos (mesmo post, mesmas url_tags, mesmo spec
devolve o **mesmo** `creative_id` para anúncios diferentes), e o anúncio fica `IN_PROCESS` logo
após a troca.

**Cuidado antes de sair trocando:** trocar o criativo de um anúncio é edição significativa e pode
devolver **o conjunto** à fase de aprendizado, não só o anúncio.

### 2026-06-08 e 2026-07-17 — Anúncio flexível (várias mídias num anúncio só): o método que funciona

**Regra:** o formato flexível, em que a Meta combina várias mídias dentro de um mesmo anúncio,
se cria com **`media_sourcing_spec` + `contextual_multi_ads`**. Funciona com imagem e com vídeo.

```python
object_story_spec = {
  "page_id": "<PAGE_ID>", "instagram_user_id": "<IG_ID>",
  "link_data": {                                  # ou video_data, para vídeo
    "link": "https://api.whatsapp.com/send",
    "name": "<título>", "message": "<legenda>",
    "image_hash": "<hash da mídia PRINCIPAL>",
    "call_to_action": {"type": "WHATSAPP_MESSAGE", "value": {"app_destination": "WHATSAPP"}},
    "page_welcome_message": "<JSON copiado de um criativo publicado da conta>"
  }
}
media_sourcing_spec = {                            # o POOL de variações
  "bodies": [{"text": "<legenda>"}], "titles": [{"text": "<título>"}], "videos": [],
  "images": [{"hash": h, "source": "multi_media", "opt_in_status": "opt_in"} for h in TODAS]
}
contextual_multi_ads = {"enroll_status": "OPT_IN"}   # a flag que liga o flexível
object_type = "SHARE"
# mais url_tags no criativo
```

Para vídeo: `object_story_spec.video_data` com o vídeo principal (`video_id`, `title`, `message`,
`call_to_action`, `page_welcome_message`, `image_url` do thumbnail) e
`media_sourcing_spec.videos = [{"video_id": v, "source": "multi_media", "opt_in_status": "opt_in"}, ...]`
com `images: []`.

**Pegadinhas, todas testadas:**

- `contextual_multi_ads: OPT_IN` é **obrigatório**. Sem ela o criativo não persiste como flexível.
- **Não** envie `degrees_of_freedom_spec` com `creative_features_spec.standard_enhancements` →
  erro **100 / subcode 3858504** ("defina recursos individuais"). Foi descontinuado. Basta
  **omitir** o bloco: o `contextual_multi_ads` sozinho já liga o flexível.
- **Não** coloque `whatsapp_business_phone_number_id` no criativo → erro **(#10)**. O número do
  WhatsApp vai no `promoted_object` do **conjunto**.
- Na releitura, o criativo mostra só a mídia principal mais a flag. As outras mídias do pool não
  voltam: a Meta serve dinamicamente. Isso é igual ao que um anúncio feito na interface devolve,
  então **não é sinal de erro**.
- `AdVideo(id).api_get(fields=['thumbnails'])` emite um aviso de campo não permitido mas
  **retorna** os thumbnails. Use o `.uri` do `is_preferred` como `image_url`.

**Becos sem saída já percorridos, não repetir:**

- `asset_customization_rules` para "várias variações num anúncio" — é outro modelo (uma imagem
  por posicionamento).
- `asset_feed_spec.images` sem regras — persiste, mas a **prévia fica em branco**.
- `optimization_type: DEGREES_OF_FREEDOM` com várias imagens — "Invalid parameter".
- Várias imagens na mesma `asset_customization_rule` — erro 1885878.

### 2026-06-23 — Imagem por posicionamento via API foi descontinuada (erro 2715)

**Regra:** montar 4:5 no feed e 9:16 no story dentro do mesmo anúncio via
`asset_customization_rules` **não funciona da v22 em diante**: a Meta responde **(#2715)
"Segment Asset Customization API has been deprecated"**. No caminho até esse erro ainda aparecem
dois enganos que fazem perder tempo: sem regra default vem **1885923**; com default vazia vem
**2446501**. Satisfazendo os dois, bate no 2715 mesmo assim.

**O que fazer hoje:** usar o **pool flexível** da entrada acima. Criativo com a imagem principal
4:5 em `link_data` mais os dois hashes (4:5 e 9:16) em `media_sourcing_spec.images`. Confirmado
na prévia: o feed mostra o 4:5 e o story mostra o 9:16 sem corte. Não é trava dura por
posicionamento, mas a Meta serve o formato certo em cada superfície. Alternativa: montar na
interface, que ainda tem o recurso.

### 2026-06-23 — Reusar `creative_id` não traz legenda se o criativo de origem não tiver corpo

**Regra:** ao popular uma campanha reusando criativos de outra, confira se o criativo de origem
tem texto principal. Criativos do tipo "anúncio de um post" costumam ter `video_data.message`
**vazio**, e o reuso sobe o anúncio sem legenda.

**Contexto:** dezoito anúncios subiram sem legenda numa campanha nova por reuso cego de
criativos.

**Pegadinha do thumbnail:** o hash da miniatura tem **32 caracteres**. Truncado, dá
**100/2446386 "Invalid parameter"**; omitido, dá **1443226** (miniatura é obrigatória em vídeo).

**Pegadinha de entrega no Instagram:** criativo de vídeo montado inline com botão de WhatsApp e
**sem** `page_welcome_message` é barrado com **code 1 / subcode 2875003 "An unknown error
occurred"** — mas o `error_user_msg` real é "chamada para ação não aceita, seu anúncio não será
veiculado no Instagram". Incluir o welcome resolve. Criativos que referenciam post existente
passam sem ele, porque já são posts aprovados.

### 2026-04-03 — Carrossel: desligar as opções de formato

**Regra:** em campanha de visita ao perfil do Instagram, sempre `multi_share_end_card: false` e
`multi_share_optimized: false`. O cartão final "ver mais" exige uma URL de destino que não existe
nesse tipo de campanha e quebra o anúncio em mais de dez posicionamentos. O `optimized` reordena
os slides, o que destrói carrossel com narrativa.

Em qualquer carrossel, passe `degrees_of_freedom_spec` com OPT_OUT para `carousel_to_video`,
`image_touchups` e `standard_enhancements`, senão a Meta distorce a sequência.

### 2026-04-03 — Sempre incluir CTA, e sempre passar `instagram_user_id`

**Regra:** criativo sem `call_to_action_type` sobe sem botão. Padrão: LEARN_MORE para tráfego,
SIGN_UP para leads, SHOP_NOW para vendas.

Sem `instagram_user_id` o anúncio não publica no Instagram ("seu anúncio deve ser associado a
uma conta do Instagram").

**Em criativo de vídeo, o CTA vai só dentro de `video_data.call_to_action`.** Mandar
`call_to_action_type` também no nível superior bloqueia o POST com OAuthException code 3.

---

## Conjuntos, objetivos e compliance

### 2026-06-15 — Compliance brasileiro: o erro 3858634 não é bloqueio absoluto

**Regra:** o erro **3858634 "anunciante ausente"** ao criar conjunto direto no Brasil é **falta
dos campos de compliance**, não uma proibição. Passe:

- `regional_regulated_categories: ["BRAZIL_REGULATION", "VOLUNTARY_VERIFICATION"]`
- `regional_regulation_identities: {"universal_beneficiary": "<ID>", "universal_payer": "<ID>"}`

Os IDs são o "anunciante verificado / pago por" da conta. Leia de um conjunto existente que já
está compliant (`fields=regional_regulation_identities`).

Isso **supera** a conclusão antiga de que conjunto no Brasil só se cria por `/copies`.

### 2026-07-13 — `POST /adsets` direto funciona em parte das contas

**Regra:** a exigência de compliance acima não se comporta igual em toda conta. Em algumas, o
`POST /act_XXX/adsets` direto passa sem `compliance_section` nenhum. **Tente o caminho direto
primeiro**; se vier 3858634, aí sim caia no `/copies`.

Importante não descartar o caminho direto, porque quando o evento de otimização precisa mudar o
`/copies` não resolve (ver entrada seguinte).

### 2026-07-13 — O evento de otimização é IMUTÁVEL num conjunto publicado (erro 3260011)

**Regra:** não dá para trocar `promoted_object.custom_event_type` (de Compra para Início de
Finalização, por exemplo) num conjunto que já existe. A API devolve **3260011**. Consequência:
**`/copies` e `duplicate-campaign --deep` não servem** quando o objetivo é mudar o evento, porque
o conjunto copiado vem com o evento do original colado e travado.

**Como fazer:** duplicar só a campanha, criar o conjunto **novo** já com o `promoted_object`
certo, e criar os anúncios reusando os mesmos `creative_id` (mantém url_tags e o teste limpo).
Se usou `--deep`, **apague o conjunto copiado**: esquecido ali, ele gasta com o evento errado e
divide o orçamento do CBO.

### 2026-07-13 — O enum é `INITIATED_CHECKOUT`, não `INITIATE_CHECKOUT`

Particípio. O outro devolve erro #100 listando os válidos.

### 2026-06-15 — Otimização por Lead em campanha nova de clique para WhatsApp é impossível via API

**Regra:** `LEAD_GENERATION` em campanha CTWA só existe em campanhas antigas (é grandfathered).
Em campanha nova, todo caminho via API falha:

- criar conjunto com `LEAD_GENERATION` → **2490408**
- mudar um conjunto de `CONVERSATIONS` para `LEAD_GENERATION` → **2490408**
- `/copies` de um conjunto Lead antigo para campanha nova → **2490408**
- `OFFSITE_CONVERSIONS` + `custom_event_type: LEAD` → **2446814**
- cópia profunda da campanha inteira → **1885194** ("cópia muito grande", o limite síncrono é
  de pouquíssimos objetos)

**O que funciona:** via API, só `CONVERSATIONS`. Para ter Lead numa campanha nova, **duplicar
pela interface** (o duplicar do Ads Manager roda no servidor e preserva a otimização antiga) e
depois ajustar o resto via API.

**Fluxo validado:** a API monta campanha e conjunto como `CONVERSATIONS` com targeting e
compliance corretos → o operador duplica na interface e troca a meta para leads → a API retoma a
duplicata e corrige o resto. Atenção: ao duplicar pela interface o conjunto volta com
`targeting_automation.advantage_audience: 1` (expansão ligada). Para remarketing puro, zerar.

### 2026-06-10 — Mensagem de boas-vindas é incompatível com otimização por Lead

**Regra:** em conjunto com `optimization_goal: LEAD_GENERATION` e destino WhatsApp, nenhum
criativo com `page_welcome_message` pode ser vinculado: **code 100 / subcode 2490163** ("a
otimização e a configuração do Messenger são incompatíveis"). Vale para criar, atualizar, reusar
criativo já publicado e até duplicar. A interface consegue; a API não.

**Como contornar:** montar os criativos **sem** `page_welcome_message`, mantendo o botão e o link
de WhatsApp. Se precisar de mensagem pré-preenchida, jogue o texto no próprio link
(`api.whatsapp.com/send?text=...`), que não dispara o bloqueio.

**Como pausar um anúncio preso nessa situação:** o pause sozinho também é barrado pelo 2490163,
porque a Meta revalida o criativo a cada edição. A saída é trocar o criativo e pausar **na mesma
chamada**:

```python
Ad(ad_id).api_update(params={"creative": {"creative_id": <sem_welcome>}, "status": "PAUSED"})
```

Para montar o criativo sem welcome sem perder nada: clone o `object_story_spec` do criativo atual
e remova só o `page_welcome_message`. Duas pegadinhas: o clone vem com `image_url` **e**
`image_hash` juntos, o que a Meta recusa com **1443051** (mantenha só o hash); e depois da troca
o `effective_status` fica `IN_PROCESS`, então confira o `configured_status` para ter certeza de
que está pausado.

### 2026-06-10 — NUNCA usar ARCHIVED como substituto de PAUSED

**Regra:** quando o pause via API está bloqueado, arquivar parece a saída. **Não é.** Arquivar
some da interface (fica atrás do filtro "arquivado") e **não dá para desarquivar via API**:
mudar o status de um anúncio arquivado devolve **1885088**. Curiosamente renomear funciona, só
a transição de status é bloqueada. O anúncio fica preso, só recuperável pela interface.

Se o pause estiver bloqueado, peça ao operador para pausar pela interface, ou resolva o conflito
de otimização. Nunca arquive.

**Contexto:** 37 anúncios arquivados como "pause reversível" sumiram da interface do operador e
não voltaram via API. Tiveram que ser recriados.

### 2026-07-28 — Conjunto de clique para WhatsApp: a cascata de erros engana

**Regra:** confirma-se a regra "conjunto CTWA na interface, anúncio pela API". O que engana é a
**ordem dos erros**, porque os três primeiros mandam para o caminho errado:

1. duplicar conjunto por `/copies` → **2446886**
2. criar conjunto sem destino → **2490408**
3. com `promoted_object: {page_id, whatsapp_phone_number}` → **1487246 "este número não está
   vinculado à sua conta"**. **Não caia nessa:** o número está certo. O conjunto que roda não
   declara número, usa `{"page_id": ..., "smart_pse_enabled": false}` e o WhatsApp vem da página.
   Sempre leia o `promoted_object` cru de um conjunto que **entrega** antes de montar.
4. com o promoted_object certo → **1885423**: a API só concede janela de atribuição de **1 dia
   de clique** nesse objetivo, enquanto conjuntos criados pela interface ficam com **7 dias**
5. com 1 dia → **2446886 "sua página não está vinculada a uma conta do WhatsApp"** (parede final)

**Consequência de análise, importante:** conjunto criado pela API (1 dia) e conjunto criado pela
interface (7 dias) têm janelas diferentes, então **o custo por lead entre os dois não é comparável**.
O de 1 dia sempre parece pior. Para comparar, crie os dois pela interface.

**Como saber se é limitação da API ou conta quebrada:** puxe insights de 7 dias do conjunto que
está rodando. Se está gerando conversa, a página está saudável e o problema é só o caminho.

### 2026-07-17 — Erro 1885648 ao ativar conjunto em CBO: piso de gasto maior que o orçamento

**Regra:** **100 / subcode 1885648** ao ativar um conjunto em CBO significa que a soma dos
`daily_min_spend_target` dos conjuntos ativos passou do orçamento da campanha. Acontece
tipicamente depois de **baixar** o orçamento do CBO: os pisos herdados de duplicações antigas
deixam de caber.

**Correção:** zerar o `daily_min_spend_target` dos conjuntos, ou subir o orçamento.

### 2026-06-01 — Campanha ABO exige `is_adset_budget_sharing_enabled`

Sem esse campo, a criação falha com erro 4834011. Passe `True` ou `False`, tanto faz, mas passe.

---

## Higiene ao subir em lote

### 2026-06-01 — Nunca deixar o sufixo "- Copy"

Ao duplicar, remova o " - Copy" do nome. Polui o gerenciador e depois alguém tem que limpar
setenta anúncios na mão.

### 2026-06-01 — O nome do anúncio é a chave de deduplicação, não o ID do criativo

**Regra:** antes de adicionar anúncios a um conjunto, liste os existentes e compare **por nome**.
A API deixa criar dois anúncios com o mesmo nome e IDs de criativo diferentes, mas na prática é o
mesmo anúncio duas vezes.

**Contexto:** uma campanha subiu com 35 anúncios por conjunto, dos quais 14 eram duplicatas.

### 2026-06-01 — Nunca misturar vídeo e estático no mesmo conjunto

Formatos diferentes competem de forma desigual pela mesma verba. Vídeo em conjunto próprio,
estático em conjunto próprio.

### Rate limit

Contas com acesso de desenvolvimento têm teto baixo. Scripts que sobem lote devem ser **gentis e
resumíveis**: deduplicar por nome, cachear hash e criativo, tentar de novo no código 17 com
espera curta, e **sair sozinhos** depois de N tentativas. Processo de retry solto vira zumbi e
trava a conta a noite inteira. Nos códigos 17, 32 e 80004, espere 60 segundos.

### Upload de imagem local

`create.py image` só aceita `--url`. Para arquivo no disco:

```python
img = AdImage(parent_id=ACCOUNT_ID)
img[AdImage.Field.filename] = caminho
img.remote_create()
image_hash = img[AdImage.Field.hash]
```

---

## Segmentação

### 2026-06-16 — Receita: conjunto só iPhone recente, só Instagram

Segmentação por aparelho como aproximação de renda. Corta os modelos antigos, que hoje custam o
mesmo que um Android intermediário usado.

```json
"user_os": ["iOS"],
"user_device": ["iphone 13","iphone 13 mini","iphone 13 pro","iphone 13 pro max",
                "iphone 14","iphone 14 plus","iphone 14 pro","iphone 14 pro max",
                "iphone 15","iphone 15 plus","iphone 15 pro","iphone 15 pro max",
                "iphone 16","iphone 16 plus","iphone 16 pro","iphone 16 pro max","iphone 16e"],
"publisher_platforms": ["instagram"],
"instagram_positions": ["stream","story","reels","explore_home","profile_feed","ig_search"],
"targeting_relaxation_types": {"lookalike": 0, "custom_audience": 0}
```

**Não existe "13 para cima" automático:** é lista literal, em minúsculas, com o nome exato.
Modelo novo não entra sozinho, tem que ser adicionado à mão.

A última linha é **obrigatória** com segmentação apertada: sem desligar a expansão, a Meta fura a
segmentação que você acabou de montar.

**Trade-off para avisar antes de recomendar:** subir o piso encolhe o público e sobe o CPM. O
salto de qualidade grande é de "todo mundo" para "13+"; de 13 para 15 o ganho é marginal e custa
alcance. E não combine corte de aparelho com corte de posicionamento no mesmo conjunto que já
roda: separe em conjunto novo para não zerar o aprendizado.

### 2026-06-10 — Página e Instagram não precisam estar vinculados entre si

**Regra:** para anunciar com uma página e um perfil de Instagram que não estão conectados entre
si, basta o **Instagram estar vinculado à conta de anúncios** (Configurações do Negócio → conta
de anúncios → Contas do Instagram). Com isso ele aparece como identidade selecionável.

**Como diagnosticar rápido:** liste os perfis da conta (`act_XXX/instagram_accounts`). Se o
perfil desejado não está lá, é esse o problema. Vincular resolve, sem precisar da senha do
perfil: basta ser administrador do Business Manager.

**Contexto:** horas perdidas investigando o vínculo página ↔ perfil, que a Meta de fato apertou
em 2023 e 2024, quando o gatilho real era o vínculo perfil ↔ conta de anúncios.

---

## Decisões que são do operador, não do Claude

Estas não são limitações técnicas: são escolhas que variam por conta. O Claude **pergunta antes**,
não decide sozinho.

- **Posicionamentos.** Se o operador tirou o Facebook de propósito, não devolver por conta
  própria achando que foi descuido. Perguntar antes de mexer em posicionamento.
- **Orçamento.** Toda alteração de verba é confirmada antes.
- **Ativar qualquer coisa.** Criar é sempre PAUSED; ativar exige confirmação.
- **Pausar campanha inteira ou apagar objeto.** Sempre confirmar.
