# Skill de Google Ads

Dá ao Claude Code controle das suas contas de Google Ads pela API oficial, com scripts Python que
rodam na sua máquina. Leitura por GAQL, escrita por mutate operations.

Você conversa em português, ele opera a conta:

- "quais campanhas estão gastando mais que R$ 100 por conversão nos últimos 7 dias?"
- "quais termos de busca estão queimando verba sem converter?"
- "cria uma campanha de search com essas 20 keywords"
- "por que essa PMax não está gastando?"
- "quanto custa a palavra 'dentista em campinas' e quanta busca ela tem?"

## Instalação

```bash
pip3 install google-ads google-auth-oauthlib protobuf
cp .env.example .env
python3 scripts/setup.py full
```

O `setup.py full` confere o que falta, abre o navegador para você autorizar e testa a conexão.

**Antes disso, leia [references/setup-google-ads-api.md](references/setup-google-ads-api.md).** O
Google exige quatro peças independentes (conta MCC, developer token, projeto no Cloud, OAuth) e
depois o acesso às contas dos clientes. É mais burocrático que a Meta, e o arquivo cobre cada tela,
cada erro e o que dizer ao cliente na hora de pedir acesso. Ou simplesmente peça ao Claude:
*"me ajuda a configurar a skill de google ads"*.

Para conferir se ficou de pé:

```bash
python3 scripts/read.py accounts
```

## O que tem aqui

| Arquivo | Para que serve |
|---|---|
| [SKILL.md](SKILL.md) | a skill: todos os comandos e as regras de segurança |
| [aprendizados.md](aprendizados.md) | erros e acertos reais operando pela API, com os códigos de erro e o que significam de verdade |
| [references/setup-google-ads-api.md](references/setup-google-ads-api.md) | setup do zero: MCC, developer token, Cloud, OAuth, acesso às contas dos clientes |
| [references/api-reference.md](references/api-reference.md) | queries GAQL úteis e referência de campos |
| [references/youtube-remarketing-internal-api.md](references/youtube-remarketing-internal-api.md) | públicos de "viu vídeo" no YouTube, que a API oficial não cria |
| [contas.yaml](contas.yaml) | cadastro dos seus clientes: nome → customer_id |

## Scripts

| Script | Função |
|---|---|
| `setup.py` | setup interativo: `check`, `oauth`, `test`, `full` |
| `read.py` | campanhas, ad groups, keywords, anúncios, search terms, negativas, extensões, quality score |
| `insights.py` | métricas e breakdowns (conta, campanha, ad group, keyword, diário, dispositivo, hora) |
| `create.py` | campanhas, ad groups, keywords, RSAs, sitelinks, callouts, negativas |
| `update.py` | status, orçamento, lances |
| `delete.py` | remover keywords, negativas, anúncios |
| `update_tracking.py` | modelo de rastreamento e UTM (dry-run por padrão) |
| `keyword_planner.py` | pesquisa de keywords: volume, CPC, competição, histórico |
| `set_campaign_settings.py` | idioma, localização e outras configurações de campanha |
| `mirror_demand_gen.py` | copia anúncios de Demand Gen entre ad groups (contorna o `AD_SHARING_NOT_ALLOWED`) |

## Segurança

- Credenciais ficam só no `.env`, que está no `.gitignore`. Nada sai da sua máquina além das
  chamadas para a própria API do Google.
- **Criação nasce PAUSED.** Ativar exige a sua confirmação.
- Orçamento, exclusão e ativação sempre pedem confirmação.
- **Orçamento é em centavos** no `update.py`: R$ 1.600,00/dia é `160000`. Passar `1600` seta R$ 16.
  Está no `aprendizados.md` porque já aconteceu.

Leia o [disclaimer no README principal](../README.md#disclaimer-use-com-responsabilidade) antes da
primeira escrita numa conta real.
