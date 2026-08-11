# Aprendizados — Google Ads via API

Erros e acertos reais operando contas pela API do Google Ads. Cada entrada aqui custou tempo (ou
dinheiro) para alguém descobrir. **O Claude DEVE ler este arquivo antes de criar qualquer objeto
na conta.**

Os IDs foram trocados por placeholders. O que importa é o padrão, não o número.

---

## Ambiente e execução

### SDK trava no macOS sem `GRPC_DNS_RESOLVER=native`

`client.get_service("GoogleAdsService")` pode dar hang infinito no macOS: o resolver DNS c-ares do
gRPC trava em algumas configurações de rede.

- **Solução:** setar `GRPC_DNS_RESOLVER=native`. A `lib/__init__.py` já faz isso, mas em alguns
  contextos o gRPC carrega antes — por isso **também passar externamente** na chamada:
  ```bash
  GRPC_DNS_RESOLVER=native python3 scripts/read.py campaigns --customer-id 1234567890
  ```
- Se travar em `get_service()`, a primeira coisa a conferir é essa variável.

### Hang volta com grpcio ≥ 1.80 mesmo com resolver native — faltava DEADLINE

Sintoma diferente, mesma cara: o cliente autentica, o TCP 443 responde, mas a **iteração do stream**
em `service.search(...)` congela para sempre porque a chamada não tem deadline.

- **Correção (já aplicada na lib):** `RPC_TIMEOUT = float(os.environ.get("GOOGLE_ADS_RPC_TIMEOUT", "120"))`,
  passado como `timeout=` no `service.search()` do `run_query`. Para afrouxar numa execução:
  `GOOGLE_ADS_RPC_TIMEOUT=180 ...`.
- Os `mutate_*` são chamadas unárias e **não** travavam — só o stream de leitura precisava de deadline.
- **Diagnóstico rápido:** rodar um `service.search(..., timeout=20.0)` mínimo. Se funciona com deadline
  e trava sem, é isso.

### Credenciais por cliente — nunca confundir

Contas em MCCs diferentes exigem credenciais diferentes. O padrão é um `.env` por perfil:

```bash
# conta padrão (.env)
GRPC_DNS_RESOLVER=native python3 scripts/read.py campaigns --customer-id 1234567890

# cliente com credenciais próprias (.env.clientex)
GOOGLE_ADS_ENV=clientex GRPC_DNS_RESOLVER=native python3 scripts/read.py campaigns --customer-id 9876543210
```

Rodar o script com o `.env` errado costuma dar erro de permissão, mas **pode** dar pior: encontrar a
conta pelo MCC errado e agir nela. Conferir o perfil antes de qualquer escrita.

---

## Unidades: onde o dinheiro se perde

### `update.py campaign --budget` espera CENTAVOS, não reais nem micros

O script faz `int(args.budget) * 10000` (centavos → micros). Para um orçamento de **R$ 1.600,00/dia**,
o valor a passar é **160000**. Passar `1600` seta **R$ 16,00/dia** — um corte de 99%, não um aumento.

Caso real: subindo o orçamento de R$1.300 para R$1.600/dia, passei `--budget 1600`. A campanha ficou
em R$16/dia por cerca de um minuto, até eu conferir o valor real via GAQL e ver o erro.

**Como aplicar:** SEMPRE conferir o resultado depois de mexer em orçamento, com leitura direta de
`campaign_budget.amount_micros` — não confiar no "status: updated" do script, que não ecoa o valor
final em reais. Um erro de unidade passa em silêncio. Fórmula: reais → centavos é `reais * 100`.

### `cost_micros` na leitura

Tudo que é dinheiro na API vem em micros (`1_000_000` = R$ 1,00). Os scripts já dividem na saída,
mas ao escrever GAQL na mão, dividir.

---

## Criação de campanhas

### PMax: dois campos obrigatórios que a API não avisa direito

1. **Orçamento dedicado:** `budget.explicitly_shared = False`. Sem isso →
   `BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET`. PMax com Maximizar Conversões não aceita
   orçamento compartilhado. (Já corrigido no `create.py`, vale para todas as campanhas.)
2. **Brand Guidelines:** contas com Brand Guidelines ligado por padrão para PMax exigem
   BUSINESS_NAME + LOGO quadrado vinculados como CampaignAsset **já na criação**
   (`REQUIRED_BUSINESS_NAME_ASSET_NOT_LINKED` / `REQUIRED_LOGO_ASSET_NOT_LINKED`). Para criar o casco
   via API, setar `campaign.brand_guidelines_enabled = False` no ramo PMAX. Nome de negócio e logo
   entram no asset group depois, pela interface.

**Limite do `create.py` para PMax:** cria só o casco (campanha + orçamento + lance). NÃO cria asset
group nem assets (URL final, headlines, descrições, imagens, logo, vídeo, search themes) — isso
continua sendo feito na UI. A campanha nasce PAUSED e não ativa sem ao menos um asset group válido.

### Campos obrigatórios que mudaram de tipo

- `contains_eu_political_advertising` é **enum**, não boolean. Valor `3` =
  DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING.
- `maximize_clicks` não funciona como atributo direto. Usar `manual_cpc.enhanced_cpc_enabled = False`
  como fallback.
- Nome de budget precisa ser único na conta. O script usa timestamp no nome para não colidir com
  budgets órfãos.
- RSA: headline ≤ 30 caracteres, description ≤ 90.

### Sitelink: `final_urls` fica no Asset pai, não no SitelinkAsset

`SitelinkAsset` tem só `link_text`, `description1`, `description2`, `start_date`, `end_date`,
`ad_schedule_targets`. A URL vai no `Asset`:

```python
a = asset_op.create              # Asset
a.sitelink_asset.link_text = "Texto"
a.final_urls.append("https://...")   # correto: no Asset, não em sitelink_asset
```

Limites: `link_text` ≤ 25, `description1/2` ≤ 35, `callout_text` ≤ 25. Callout e structured snippet
seguem o mesmo padrão: criar o asset → criar o CampaignAsset com o `field_type` certo (SITELINK,
CALLOUT, STRUCTURED_SNIPPET). O header "Tipos" é válido em pt-BR.

### Keyword com policy violation NON_FAMILY_SAFE — como adicionar com isenção

Nichos sensíveis disparam `NON_FAMILY_SAFE` (Moderately Restricted, `is_exemptible: true`). Para
adicionar com isenção, usar `PolicyViolationKey` (e não `ExemptPolicyViolationKey`, que não existe):

```python
from google.ads.googleads.v24.common.types.policy import PolicyViolationKey
exempt = PolicyViolationKey(policy_name="NON_FAMILY_SAFE", violating_text="<keyword>")
op.exempt_policy_violation_keys.append(exempt)
```

Enviar a keyword problemática em operação separada das keywords limpas.

### Campanha PAUSED às vezes não aparece na interface

Já houve relato de campanha criada como PAUSED não aparecer na UI nem com o filtro de status certo.
Se o operador reclamar disso, a saída é criar ENABLED e pausar na mão na interface logo depois —
**mas só com o ok explícito dele**, porque isso significa campanha ativa por alguns segundos.

---

## Lance, meta de conversão e público (o que a skill não cobre)

`create.py`/`update.py` **não** cobrem bidding strategy, `asset_group_signal`, audience nem
conversion goal. Para esses, mutate custom via SDK (`sys.path` para `scripts`, `from lib import init_client`):

- **Trocar bidding strategy:** mascarar o **subcampo folha**, nunca a mensagem.
  `op.update.maximize_conversion_value.target_roas = 0.0` + mask `["maximize_conversion_value.target_roas"]`
  = Maximizar Valor puro. `op.update.maximize_conversions.target_cpa_micros = 0` + mask
  `["maximize_conversions.target_cpa_micros"]` = Maximizar Conversões puro. Mascarar a mensagem
  inteira → `FIELD_HAS_SUBFIELDS`; mensagem vazia some no `protobuf_helpers.field_mask`.
- **Value bidding precisa de histórico:** trocar para MAXIMIZE_CONVERSION_VALUE numa campanha sem
  conversões suficientes do goal alvo → `NOT_ENOUGH_CONVERSIONS` (comum em Demand Gen/YouTube com
  evento novo). Fallback: Maximizar Conversões, que não tem esse mínimo.
- **Trocar a meta de conversão (custom goal):** `ConversionGoalCampaignConfigService`, update em
  `customers/{cid}/conversionGoalCampaignConfigs/{campaign_id}`, com `goal_config_level=CAMPAIGN` +
  `custom_conversion_goal=customers/{cid}/customConversionGoals/{id}`. **Esse service não aceita
  `validate_only`.**
- **`asset_group_signal` é imutável:** para trocar o público-sinal, `remove` o antigo (resource_name)
  + `create` o novo (audience ou search_theme) no mesmo mutate. Audience dedicada via `AudienceService`
  (dimensions → audience_segments → user_list); remover = update com status REMOVED (não tem `remove`).

---

## Demand Gen com `use_audience_grouped=True`

Campanhas Demand Gen criadas com `campaign.audience_setting.use_audience_grouped = True` têm dois
bloqueios **imutáveis**:

1. Não aceitam critério individual de `user_list` via API
   (`CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET`), nem na criação nem no update.
2. `AD_SHARING_NOT_ALLOWED`: ads de Demand Gen não podem ser reutilizados em vários ad groups — cada
   ad group precisa das suas próprias instâncias do criativo.

**Dá para fazer 100% via API, sem UI.** A limitação é só na *forma* de anexar o público — em vez de
critério de user_list, criar um `Audience` e anexá-lo como critério `AUDIENCE`. Receita validada:

1. `AudienceService.mutate_audiences` → `create` com `dimensions[].audience_segments.segments[].user_list`
   (o público-alvo) e `exclusion_dimension.exclusions[].user_list` (as exclusões). Tipos:
   `AudienceDimension`, `AudienceSegment`, `ExclusionSegment`.
2. `AdGroupService.mutate_ad_groups` → cria o ad group normalmente (não setar `type`).
3. `AdGroupCriterionService.mutate_ad_group_criteria` → um único critério com
   `audience.audience = <resource_name da Audience>`.
4. **O Google espelha sozinho** no ad group os `user_list` (o positivo e todos os negativos da
   `exclusion_dimension`) e a demografia. **Não criar esses critérios na mão** — é aí que estoura o
   `CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET`.
5. Ads: como `AD_SHARING_NOT_ALLOWED` continua valendo, copiar o criativo com
   `c.ad.demand_gen_video_responsive_ad._pb.CopyFrom(src._pb)` + `name` + `final_urls`. Exemplo pronto
   em `scripts/mirror_demand_gen.py`.

**Pegadinhas:**

- Sem `household_income` nas `dimensions`, o Google cria as 7 faixas de renda **todas incluídas**
  (0 negativas) = sem filtro nenhum. Com `household_income`, ele deriva as negativas. Conferir por
  `ad_group_criterion.income_range` + `negative`.
- `validate_only` em `mutate_ad_groups` **não é kwarg** — montar `MutateAdGroupsRequest` (mesmo padrão
  do `partial_failure`).
- Para só *adicionar* uma exclusão a uma Audience existente: update com mask
  `exclusion_dimension.exclusions`, preservando as antigas na lista (o update substitui o campo inteiro).

---

## Públicos

### Customer Match: upload não é mais pela Ads API → Data Manager API

O `OfflineUserDataJob` da Ads API responde `CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE` — o Google
descontinuou esse caminho. O upload agora é na **Data Manager API**:

- `POST https://datamanager.googleapis.com/v1/audienceMembers:ingest`, escopo OAuth
  `https://www.googleapis.com/auth/datamanager` (ativar a API no projeto do Cloud e gerar um refresh
  token novo — o escopo antigo não serve).
- Corpo: `destinations[].operatingAccount{product:"GOOGLE_ADS", accountId}` + `productDestinationId=<user_list_id>`;
  `audienceMembers[].compositeData.userData.userIdentifiers[]` com `emailAddress`/`phoneNumber`
  (valor = hash, `encoding:"HEX"`); `consent` GRANTED; `termsOfService: ACCEPTED`.
- A **user list** ainda se cria pela Ads API (`UserListService`, `crm_based_user_list` CONTACT_INFO,
  `membership_life_span` máx **540** dias).
- Normalização do Google antes do hash: gmail remove ponto e `+sufixo`; telefone com `+` e DDI.
- **Demand Gen** recusa exclusão por criterion (audience grouped) → editar o `Audience` asset
  (`exclusion_dimension.exclusions`, field mask = `exclusion_dimension.exclusions`).

### Público de YouTube (viu vídeo) não se cria pela API oficial

A API oficial **não cria nem edita** públicos de "usuários do YouTube" (viu vídeo, viu vídeo
específico, inscritos) — só lê, via GAQL `user_list`. Criar/editar exige os endpoints RPC internos do
painel, autenticados por cookie de sessão. Esquemas, payloads, limites e a receita de automação estão
em `references/youtube-remarketing-internal-api.md`. Resumo do que dói: limite de ~40 vídeos por lista,
o `Update` substitui a lista inteira, o token `x-framework-xsrf-token` gira a cada sessão, e nada disso
roda em servidor sem navegador logado.

### Públicos em campanhas Search: sempre Observação

- Em Search, público é **Observação**, nunca Segmentação. Segmentação restringe o alcance ao público
  escolhido e corta impressão à toa.
- **Ao criar ad group via API**, o Google pode herdar a configuração de segmentação dos ad groups que
  já existem na campanha. Conferir depois de criar.
- **Verificar:** `campaign.targeting_setting.target_restrictions`. `bid_only: True` para a dimensão
  AUDIENCE = Observação (certo). `bid_only: False` = Segmentação (restritivo, corrigir).
- **Corrigir:** update em `campaign.targeting_setting` com
  `target_restrictions: [{targeting_dimension: AUDIENCE, bid_only: True}]`.

---

## Análise e otimização

### Prioridade de otimização em Search: QS → lance → orçamento

Não pular etapa:

1. **Quality Score primeiro.** QS ruim = Ad Rank baixo = parcela de impressão baixa = leilão perdido.
   Melhorar QS resolve ISS sem gastar mais. QS baixo em keyword de volume alto → revisar a relevância
   do RSA e a experiência da landing page. QS 5 ou menos com CPA alto → pausar a keyword.
2. **Lance depois**, e só quando o QS estabilizar (6+).
3. **Orçamento por último.** Aumentar verba com QS ruim é jogar dinheiro fora. Antes de aumentar,
   confirmar que a campanha está gastando o orçamento atual: campanha que gasta 50% do orçamento **não**
   é budget-limited, é rank-limited — mais verba não muda nada.

### Teoria do bolo de cenoura: relevância tripla em Search

QS alto e CPC mínimo dependem de **três elos alinhados**: termo de pesquisa → headline do anúncio →
página de destino. Quebrar qualquer um mata a Ad Relevance e a Landing Page Experience, que são as
duas componentes de QS que o gestor de fato controla.

**Na criação de RSA:**

- Definir o grupo semântico do ad group antes de escrever a primeira headline.
- Headline 1 espelha o termo de pesquisa mais frequente daquele ad group (keyword insertion explícita
  ou cópia semântica exata).
- A LP precisa responder à mesma intenção: se a keyword é "curso de renda fixa", o H1 da LP fala de
  renda fixa.
- **Nunca** usar headline genérica ("Comece Agora", "Aprenda Já") como headline 1 em ad group de
  intenção específica.
- **Ler a LP antes de escrever** (scraping ou o próprio navegador): extrair H1, título e promessa
  principal, e usar os argumentos reais da página nas demais headlines.
- Se a conta tem uma LP genérica só para tudo, aceitar o risco de Landing Page Experience média e
  compensar com headline ainda mais específica. É uma limitação da conta, não um bug para consertar
  na campanha.

**Sinais de relevância quebrada:** Ad Relevance "abaixo da média" = a headline não reflete o termo.
Landing Page Experience "abaixo da média" = o conteúdo da LP não bate com a intenção.

### PMax: evento de otimização, benchmark de tCPA e trava de lance

Lições de uma análise que saiu errada por **inferir** configuração em vez de confirmar:

1. **O evento de otimização NÃO se descobre por `campaign_conversion_goal` nem por
   `selective_optimization`.** O `campaign_conversion_goal` devolve as metas padrão da conta para
   TODAS as campanhas (parece que a campanha bida para tudo, e não é isso). O
   `campaign.selective_optimization.conversion_actions` volta vazio até em campanha que otimiza para
   um evento específico. **Regra: perguntar ao operador ou olhar a origem real das conversões da
   campanha. Não inferir.**
2. **Benchmark de tCPA só vale no MESMO evento de conversão.** Comparar tCPA entre PMax que perseguem
   eventos diferentes é erro grosseiro — o CPA de uma campanha de venda não serve de referência para
   lance de campanha de lead, ainda que as duas apareçam lado a lado no relatório.
3. **PMax que não gasta: primeira hipótese é a trava de lance, não "está aprendendo".** tCPA abaixo do
   CPA real do evento estrangula a campanha, que simplesmente não entra em leilão. Caso real: ao soltar
   a trava, a campanha começou a gastar no mesmo dia. Só culpar a rampa de aprendizado depois de
   conferir se o limite de lance é compatível com o CPA real daquele evento.
4. **Campanha-espelho.** Vale manter na conta uma campanha que serve de molde e clonar a partir dela
   (lance, metas, ativos, públicos), mudando só o que precisa mudar. Ao montar campanha nova num
   cliente que já tem esse padrão, partir do espelho em vez de reinventar a estrutura.
5. **Postura (a meta-lição):** não empurrar estratégia sem confirmar o terreno — evento de otimização,
   papel da campanha, o que já foi testado. Confirmar a configuração real primeiro, recomendar depois.

### Bloquear apps na PMax: o catch-all morreu e categoria não basta

Contexto: PMax de lead vazando inventário in-app (jogos, apps de clima, "ganhe dinheiro").

1. **`adsenseformobileapps.com` não funciona mais.** Como `CustomerNegativeCriterion.placement.url`
   retorna `INVALID_ARGUMENT: "Invalid placement URL"`. O catch-all clássico foi descontinuado.
2. **Exclusão por CATEGORIA de app (`mobile_app_category`) não é totalmente honrada pela PMax.** Uma
   conta com 48 categorias e 40 apps já excluídos continuava vazando apps mainstream. Completar
   categoria ajuda pouco.
3. **O que funciona:** excluir **apps específicos** como `CustomerNegativeCriterion` com
   `mobile_application.app_id = "2-<package>"` (2 = Android/Google Play). O mutate em lote precisa de
   request object (`MutateCustomerNegativeCriteriaRequest` com `partial_failure=True`) — o kwarg
   `partial_failure=` direto no método não existe.
4. **Diagnóstico de onde a PMax está servindo:** `performance_max_placement_view` (traz
   `placement_type`, `display_name`, `target_url`, `metrics.impressions`; não traz custo). Filtrar
   `placement_type = MOBILE_APPLICATION`.
5. **A verdade estrutural para dizer ao cliente:** não dá para garantir PMax 100% livre de app. Sobra
   blocklist de apps específicos, que é enxugar gelo. Se a qualidade do lead exige zero app, a solução
   é estrutural (tirar o lead-gen da PMax), não exclusão.

```python
svc = client.get_service("CustomerNegativeCriterionService")
op = client.get_type("CustomerNegativeCriterionOperation")
op.create.mobile_application.app_id = "2-com.exemplo.app"
req = client.get_type("MutateCustomerNegativeCriteriaRequest")
req.customer_id = cid; req.operations.extend([op]); req.partial_failure = True
svc.mutate_customer_negative_criteria(request=req)
```

---

## Como registrar um aprendizado novo

Formato: título com o sintoma (não com a solução), **Regra** com o que fazer, e o contexto do caso
real sem nome de cliente nem ID real. Se o erro tiver código da API, colocar o código no texto — é
por ele que a busca acontece da próxima vez.
