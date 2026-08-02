# Padrões por tipo de campanha

Configuração validada por tipo. O Claude deve consultar este arquivo **antes de criar qualquer
campanha** e aplicar o padrão correspondente.

Se o tipo não estiver documentado aqui, **a conta é a fonte de verdade**: busque uma campanha
similar que já funciona nela e use como molde. Cada conta tem particularidades que não estão em
manual nenhum.

---

## Fluxo obrigatório

### Antes de criar

1. Listar campanhas existentes com objetivo parecido:
   ```
   read.py campaigns --account act_XXX --status ACTIVE
   ```
2. Abrir uma delas por inteiro:
   ```
   read.py adsets-by-campaign --campaign XXX
   read.py ads-by-campaign --campaign XXX
   read.py creative --id XXX
   ```
3. Extrair os padrões da conta: `destination_type`, `promoted_object`, `optimization_goal`,
   `instagram_user_id`, `degrees_of_freedom_spec`, `url_tags`, `page_welcome_message`,
   `attribution_spec`, identidades de compliance.
4. Usar como base, mudando só o que precisa mudar: nome, orçamento, criativo, segmentação.

### Depois de criar

1. Reler o anúncio e conferir que o `effective_status` não é `DISAPPROVED`.
2. Rodar o **pré-voo dos quatro campos** (ver `SKILL.md`): welcome message, url_tags, message,
   title. Com leitura aninhada.
3. Abrir a prévia:
   ```
   read.py preview --creative XXX --format all
   ```
4. Corrigir tudo **antes** de reportar sucesso ao operador.

---

## Visita ao perfil do Instagram

Leva o usuário ao perfil, não a um site.

| Nível | Campo | Valor |
|---|---|---|
| Campanha | `objective` | `OUTCOME_TRAFFIC` |
| Campanha | `special_ad_categories` | `[]` |
| Conjunto | `optimization_goal` | `VISIT_INSTAGRAM_PROFILE` |
| Conjunto | `destination_type` | `INSTAGRAM_PROFILE` |
| Conjunto | `billing_event` | `IMPRESSIONS` |
| Conjunto | `promoted_object` | `{"instagram_profile_id": "<IG_ID>"}` |
| Criativo | `instagram_user_id` | obrigatório |

**Regras críticas:**

- `multi_share_end_card: false` — o cartão final "ver mais" exige uma URL de destino que não
  existe aqui, e quebra o anúncio em mais de dez posicionamentos.
- `multi_share_optimized: false` — senão a Meta reordena os slides, o que destrói carrossel com
  narrativa sequencial.
- `instagram_user_id` no criativo, sempre. Sem ele o anúncio não publica no Instagram.
- Desligar as opções de formato que distorcem o carrossel:
  ```json
  {"creative_features_spec": {
     "carousel_to_video":     {"enroll_status": "OPT_OUT"},
     "image_touchups":        {"enroll_status": "OPT_OUT"},
     "standard_enhancements": {"enroll_status": "OPT_OUT"}}}
  ```

**Exemplo completo:**

```bash
# 1. Campanha
create.py campaign --account act_XXX --name "visitas-ig" \
  --objective OUTCOME_TRAFFIC --daily-budget 1000

# 2. Conjunto
create.py adset --account act_XXX --name "publico-frio" \
  --campaign <CAMP_ID> --optimization-goal VISIT_INSTAGRAM_PROFILE \
  --billing-event IMPRESSIONS --destination-type INSTAGRAM_PROFILE \
  --promoted-object '{"instagram_profile_id":"<IG_ID>"}' \
  --targeting '{"age_min":18,"age_max":65,"geo_locations":{"countries":["BR"]},"targeting_automation":{"advantage_audience":1}}' \
  --daily-budget 1000

# 3. Criativo (carrossel)
create.py creative --account act_XXX --name "carrossel-v1" \
  --instagram-user-id <IG_ID> \
  --object-story-spec '{"page_id":"<PAGE_ID>","link_data":{"message":"<legenda>","child_attachments":[{"image_hash":"<HASH>","name":"Slide 01"}],"multi_share_end_card":false,"multi_share_optimized":false}}' \
  --url-tags "utm_source=facebook&utm_medium=cpc&utm_campaign=<nome>"

# 4. Anúncio
create.py ad --account act_XXX --name "carrossel-v1" \
  --adset <ADSET_ID> --creative '{"creative_id":"<CREATIVE_ID>"}' \
  --degrees-of-freedom-spec '{"creative_features_spec":{"carousel_to_video":{"enroll_status":"OPT_OUT"},"image_touchups":{"enroll_status":"OPT_OUT"},"standard_enhancements":{"enroll_status":"OPT_OUT"}}}'
```

---

## Clique para WhatsApp (CTWA)

O tipo mais cheio de armadilhas. Leia as entradas de CTWA em `aprendizados.md` antes de começar.

**A regra que resume tudo: o conjunto se cria na interface, os anúncios se criam pela API.**

Por quê: no Brasil o conjunto esbarra em compliance, na janela de atribuição (a API só concede 1
dia de clique, a interface entrega 7) e no vínculo da página com o WhatsApp. Já a criação de
anúncios pela API funciona bem e é onde está o ganho de tempo.

**Configuração do conjunto que funciona** (leia sempre o `promoted_object` cru de um conjunto que
já entrega, em vez de montar do zero):

| Campo | Valor |
|---|---|
| `optimization_goal` | `CONVERSATIONS`, ou `OFFSITE_CONVERSIONS` se otimizar por evento do pixel |
| `destination_type` | `WHATSAPP` |
| `billing_event` | `IMPRESSIONS` |
| `promoted_object` | `{"page_id": "<PAGE_ID>", "smart_pse_enabled": false}` — **sem** o número |
| `attribution_spec` | `[{"event_type":"CLICK_THROUGH","window_days":7}]` (só pela interface) |

Para otimizar por compra: objetivo **Vendas**, destino **Mensagens**, meta **Conversões**, e o
evento escolhido no pixel. Nesse caso o `promoted_object` leva `pixel_id` e `custom_event_type`.

**No criativo:**

- CTA `{"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP","link":"https://api.whatsapp.com/send"}}`
- `page_welcome_message` copiado literalmente de um criativo publicado da conta
- `url_tags`
- **Nunca** o `whatsapp_business_phone_number_id`: ele mora no conjunto, e no criativo dá erro
  (#10).

**Pegadinha que apaga trabalho:** duplicar uma campanha de Mensagens e trocar o objetivo para
Vendas faz a Meta **apagar todo o targeting** dos conjuntos. Os conjuntos e os nomes sobrevivem;
públicos, idade, posicionamento e aparelho voltam ao default. Tem que refazer.

---

## Tráfego para site

> A documentar quando houver padrão validado. Enquanto isso, use o fluxo "antes de criar" e
> copie uma campanha da conta.

## Geração de leads (formulário nativo)

> A documentar quando houver padrão validado.

## Conversões e vendas no site

> A documentar quando houver padrão validado. Ponto de atenção: o evento de otimização é
> imutável depois que o conjunto é publicado. Ver `aprendizados.md`, erro 3260011.

---

## Como adicionar um padrão novo

Quando um tipo novo for criado e validado (sem alerta, prévia renderizando, entregando normal),
documente aqui:

1. Nome e descrição do tipo
2. Tabela de configuração por nível
3. Regras críticas (o que quebra se não fizer)
4. Exemplo completo de comandos, **com placeholders, nunca com IDs reais**
