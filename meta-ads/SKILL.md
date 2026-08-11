---
name: meta-ads
description: "Gerencia Meta Ads (Facebook e Instagram) via SDK oficial facebook-business, com scripts Python locais. Lê campanhas, conjuntos, anúncios, criativos e insights; cria, edita, pausa, ativa, duplica e deleta objetos; busca interesses, comportamentos e geolocalizações para segmentação; troca url_tags de criativos existentes; cria dark posts e criativos; diagnostica pixel, dataset e CAPI. Use quando o usuário mencionar meta ads, facebook ads, instagram ads, gerenciador de anúncios, campanha, conjunto de anúncios, ad set, anúncio, criativo, dark post, segmentação, público, audiência, interesses, lookalike, custom audience, insights, métricas, ROAS, CPA, CPL, gasto, frequência, criar campanha, pausar campanha, ativar campanha, editar campanha, duplicar campanha ou anúncio, teste A/B, mudar orçamento, daily_budget, lifetime_budget, url_tags, UTM, clique para WhatsApp, CTWA, pixel, dataset, evento, CAPI, conversão personalizada, preview de criativo, subir anúncio, ou o nome de qualquer conta cadastrada no contas.yaml. Também dispara com /meta-ads e /meta-ads setup."
---

# Meta Ads

Gestão de Meta Ads pela API oficial. Os scripts em `scripts/` executam; os arquivos em
`references/` decidem o que executar.

## Ordem de leitura obrigatória

| Quando | Ler antes |
|---|---|
| Primeira vez, ou token não funciona | `references/setup-meta-app.md` |
| Antes de **criar** qualquer objeto | `aprendizados.md` e `references/padroes-campanha.md` |
| Antes de recomendar estratégia, estrutura, verba ou otimização | `references/metodo-operacional.md` e `../kb/meta-ads-inteligencia.md` |
| Cliente é e-commerce, negócio local ou infoproduto | o playbook do modelo em `../kb/` |
| Dúvida de campo ou endpoint da API | `references/api-reference.md` |

Não pule o `aprendizados.md`. Ele existe porque cada entrada ali já custou dinheiro real.

---

## PRÉ-VOO OBRIGATÓRIO: nunca ativar anúncio sem conferir os quatro campos

**Vem antes de qualquer ativação. Não é opcional.**

Criativo montado do zero pela API perde campos **em silêncio**: a API aceita e não reclama.

| Campo | Onde fica | O que quebra sem ele |
|---|---|---|
| `page_welcome_message` | `object_story_spec.video_data` ou `link_data` | em clique para WhatsApp, o lead abre a conversa com a caixa vazia e muitos desistem |
| `url_tags` | raiz do criativo | o CRM perde a atribuição por anúncio |
| `message` | dentro de `video_data` / `link_data` | o anúncio roda sem uma linha de texto |
| `title` | idem | cai no título default da Meta |

**Procedimento:**

1. Antes de criar, ler um criativo já publicado e performando da mesma conta, **com leitura
   aninhada** (leitura rasa devolve o spec truncado e finge que os campos não existem):
   ```
   read.py creative --id <id_de_um_criativo_bom>
   ```
2. Copiar os campos **literalmente**. Cada conta tem seu próprio modelo de mensagem de
   boas-vindas, com `template_id` próprio. Nunca remontar esse JSON na mão.
3. Depois de criar e **antes de ativar**, reler o criativo novo e conferir os quatro.
   **Se qualquer um vier vazio, abortar a ativação e avisar o operador.**

Detalhes e os casos que geraram a regra: `aprendizados.md`.

---

## Setup (primeira vez)

Quando o usuário pedir para configurar, ou for a primeira vez, conduza o setup. **Leia
`references/setup-meta-app.md` antes de começar** — ele tem o passo a passo das telas da Meta,
como gerar o token, como conseguir acesso às contas de anúncio dos clientes e a tabela de erros.
Se o usuário mandar print de alguma tela, use esse arquivo para orientar.

### 1. Dependência e credenciais

```bash
pip3 install facebook-business
python3 scripts/setup.py
```

Se não existir `.env` na raiz da skill, copie o `.env.example` e conduza o preenchimento de
`META_ADS_TOKEN` e `META_APP_ID`. Os scripts leem o `.env` sozinhos: não precisa exportar nada no
shell, e o token não vaza para outras sessões do terminal.

**Nunca peça o token colado na conversa.** Oriente o usuário a editar o `.env` direto.

O app precisa estar em modo **Live** para criar criativos e dark posts. Em modo Desenvolvimento,
só leitura funciona.

### 2. Cadastro de contas (conversacional)

Depois que o `setup.py` passar, ofereça cadastrar as contas:

1. `read.py accounts` para listar o que o token enxerga.
2. Se voltar vazio, o problema é acesso, não token: volte para `references/setup-meta-app.md`,
   etapa 3.
3. Pergunte o nome de cada cliente e preencha o `contas.yaml`: conta de anúncio, página,
   Instagram, pixel.
4. Pergunte se quer cadastrar mais algum.

Antes de qualquer operação, **leia o `contas.yaml`** para traduzir nome em ID. Se o cliente não
estiver cadastrado, pergunte os dados e ofereça adicionar.

---

## Como executar

```
python3 scripts/<script>.py <subcomando> [argumentos]
```

Interprete o pedido do usuário e rode o script certo via terminal.

### Leitura (read.py)

| Subcomando | O que faz |
|---|---|
| `accounts` | lista contas de anúncio |
| `account-details` | detalhes de uma conta |
| `campaigns` | lista campanhas (`--account act_XXX --status ACTIVE`) |
| `campaign` | detalhes de uma campanha |
| `adsets` / `adsets-by-campaign` / `adset` / `adsets-by-ids` | conjuntos |
| `ads` / `ads-by-campaign` / `ads-by-adset` / `ad` | anúncios |
| `creative` / `creatives-by-ad` | criativos |
| `preview` | prévia HTML (`--creative ID --format all`) |
| `images` / `videos` | mídias da conta |
| `activities` / `activities-by-adset` | log de alterações |
| `custom-audiences` / `lookalike-audiences` | públicos |
| `paginate` | segue URL de paginação |

### Insights (insights.py)

`account`, `campaign`, `adset`, `ad`, `async` (relatório pesado).

Parâmetros principais: `--date-preset` (`last_7d`, `last_30d`, `today`, `maximum`),
`--time-range` e `--time-ranges` em JSON, `--time-increment`, `--breakdowns` (`age,gender`,
`country`, `publisher_platform`), `--action-breakdowns`, `--action-attribution-windows`,
`--level`, `--filtering`, `--sort`, `--default-summary`, `--locale`, `--limit`, `--offset`.

### Segmentação (targeting.py)

`interests`, `interest-suggestions`, `behaviors`, `demographics`, `geolocations`, `validate`,
`reach`, `delivery`, `describe`.

### Criação (create.py)

`campaign`, `adset`, `ad`, `creative`, `image`, `video`, `custom-audience`, `lookalike`.

**Toda criação sai PAUSED.** Revisar antes de ativar.

### Edição (update.py) e exclusão (delete.py)

`update.py`: `campaign`, `adset`, `ad`, `audience-users`.
`delete.py`: `object`, `audience`.

### Avançado (advanced.py)

| Subcomando | O que faz |
|---|---|
| `swap-url-tags` | troca as url_tags de um anúncio existente |
| `duplicate-ad` | duplica anúncio com url_tags novas |
| `duplicate-adset` | duplica conjunto |
| `duplicate-campaign` | duplica campanha (`--deep` leva conjuntos e anúncios) |

Criativos na Meta são **imutáveis**: não dá para editar url_tags, URL, imagem ou texto de um
criativo que já existe. O `swap-url-tags` contorna criando um criativo idêntico com as tags
certas e trocando no anúncio.

### Pixel e datasets (dataset.py)

`list`, `get`, `create`, `stats`, `events`, `share`, `unshare`, `shared-accounts`, `diagnostics`.

O `diagnostics` devolve um resumo de saúde (`HEALTHY` / `DEGRADED` / `UNHEALTHY`) com último
disparo, eventos dos últimos 7 dias, matching automático e CAPI.

---

## Regras de segurança

1. **Criar sempre PAUSED.** Nunca criar objeto já ativo.
2. **Confirmar antes de ativar.** Sempre.
3. **Confirmar antes de deletar.** Sempre.
4. **Ativar todos os níveis.** Ao ativar uma campanha, ativar também os conjuntos e os anúncios
   dentro dela. Ordem: campanha → conjuntos → anúncios. Ativar só a campanha não veicula nada.
5. **Orçamento com confirmação.** Valores vão em centavos: `5000` é R$ 50,00. Confirme o número
   com o usuário antes de aplicar.
6. **Respeitar rate limit.** O SDK já espera 1s entre escritas. Nos erros 17, 32 e 80004,
   aguardar 60 segundos.
7. **Nunca hardcodar token.** Sempre via `.env`.
8. **Nunca atribuir resultado sem quebrar por campanha.** Ao mostrar números do nível da conta,
   detalhar por campanha antes de dizer que um resultado veio de uma campanha específica.
9. **Não decidir sozinho o que é escolha do operador:** posicionamento, verba, público e
   ativação. Perguntar.

---

## Fluxos comuns

### Criar campanha completa

**Passo 0, diagnóstico (obrigatório):**
1. Ler `references/padroes-campanha.md` para o tipo desejado.
2. Buscar uma campanha similar que já funciona na conta e inspecionar conjunto, anúncio e
   criativo.
3. Extrair os padrões da conta: `destination_type`, `promoted_object`, `optimization_goal`,
   `instagram_user_id`, `degrees_of_freedom_spec`, url_tags, mensagem de boas-vindas.
4. Usar como base. **A conta é a fonte de verdade, não o exemplo genérico da documentação.**

**Passos 1 a 5:** `create.py campaign` → `adset` → `image`/`video` → `creative` (com url_tags e
instagram_user_id) → `ad`. Tudo PAUSED.

**Passo 6, validação (obrigatório):** reler o anúncio, conferir o pré-voo dos quatro campos e
abrir a prévia (`read.py preview --creative ID --format all`). "Criado com sucesso" não garante
que renderiza. Corrigir antes de reportar sucesso.

**Passo 7, ativação:** confirmar com o usuário e ativar campanha, conjuntos e anúncios.

### Corrigir url_tags de anúncios existentes

Criativo é imutável. O caminho é duplicar: ler o criativo atual, criar um novo reusando o
`object_story_id` do original com as url_tags certas, criar o anúncio novo PAUSED no mesmo
conjunto, ativar o novo e pausar o antigo. O `advanced.py swap-url-tags` faz isso sozinho.

### Duplicar campanha para teste A/B

`advanced.py duplicate-campaign --id X --deep`, depois ajustar segmentação e nome do clone.
**Atenção:** se o objetivo do teste é mudar o evento de otimização, o `--deep` não serve. Ver
`aprendizados.md`, erro 3260011.

### Relatório de performance

`insights.py campaign --id X --date-preset last_30d --breakdowns age,gender`. Para relatório
pesado, `insights.py async`.

---

## Aprendizados (memória da skill)

O `aprendizados.md` é a memória viva desta skill. O Claude deve:

1. **Lê-lo antes de qualquer criação.**
2. **Quando o operador corrigir algo** ("faltou o CTA", "tinha que ser carrossel", "não mexe no
   posicionamento"), perguntar: "quer que eu registre isso nos aprendizados?"
3. **Registrar na hora** quando ele pedir ("anota isso", "lembra disso").
4. Usar o formato documentado no topo do arquivo, **sem nome de cliente e sem ID real** se o
   arquivo for versionado.
5. Não duplicar: conferir se já existe regra parecida antes de acrescentar.

---

## Registro de histórico (opcional, recomendado)

Se o operador mantiver uma pasta por cliente, registre toda ação de escrita (criação, edição,
pausa, ativação, exclusão) num arquivo de histórico do cliente, com: data, campanha e ID, o que
foi feito, por quê, o que se esperava, as métricas de antes, e um campo de resultado para
preencher na análise seguinte.

Uma entrada por sessão de otimização, agrupando ações relacionadas. É o que permite comparar
decisão com resultado meses depois, e é o que prova o trabalho para o cliente.

Pergunte uma vez onde ele quer esses arquivos e siga usando o mesmo lugar.
