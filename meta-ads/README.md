# Skill de Meta Ads

Dá ao Claude Code controle das suas contas de Meta Ads (Facebook e Instagram) pela API oficial, com
scripts Python que rodam na sua máquina.

Você conversa em português, ele opera o gerenciador:

- "lista as campanhas ativas do cliente X"
- "quanto gastei nos últimos 7 dias, quebrado por campanha"
- "cria uma campanha de leads com R$ 50 por dia"
- "duplica essa campanha e troca as UTMs"
- "esse pixel está saudável?"

**54 operações** em 8 scripts: leitura, métricas, segmentação, criação, edição, exclusão, duplicação
e diagnóstico de pixel.

## Instalação

```bash
pip3 install facebook-business
cp .env.example .env
```

Depois abra o Claude Code e peça: *"roda o setup da skill de meta ads"*. Ele cria o app na Meta, gera
o token, resolve o acesso às contas e cadastra seus clientes. Se preferir fazer na mão, o passo a
passo com as telas da Meta está em [references/setup-meta-app.md](references/setup-meta-app.md).

Para conferir se ficou de pé:

```bash
python3 scripts/setup.py
python3 scripts/read.py accounts
```

Se `accounts` listar suas contas, está pronto.

## O que tem aqui

| Arquivo | Para que serve |
|---|---|
| [SKILL.md](SKILL.md) | a skill: referência de todos os comandos e as regras de segurança |
| [aprendizados.md](aprendizados.md) | erros e acertos reais ao subir campanhas pela API, com os códigos de erro e o que eles significam de verdade |
| [references/setup-meta-app.md](references/setup-meta-app.md) | app, token, acesso às contas dos clientes, troubleshooting |
| [references/metodo-operacional.md](references/metodo-operacional.md) | o método: rotina de otimização, os seis parafusos, métricas, escala |
| [references/padroes-campanha.md](references/padroes-campanha.md) | configuração validada por tipo de campanha |
| [references/api-reference.md](references/api-reference.md) | referência de campos e endpoints |
| [contas.yaml](contas.yaml) | cadastro dos seus clientes: nome → IDs |
| `scripts/` | os scripts Python que falam com a API |

Para estratégia (leilão, criativo, públicos, escala, contingência), a base está em
[../kb/meta-ads-inteligencia.md](../kb/meta-ads-inteligencia.md), mais o playbook do modelo de
negócio do cliente (e-commerce, negócio local, infoproduto) na mesma pasta.

## Segurança

- O token fica só no `.env`, que está no `.gitignore`. Nada é enviado para lugar nenhum além da
  própria Meta.
- **Toda criação nasce pausada.** Ativar exige a sua confirmação.
- Orçamento, exclusão e ativação sempre pedem confirmação antes.
- Orçamento é em centavos: `5000` é R$ 50,00.
- Se for versionar o `contas.yaml` preenchido, lembre que ele leva os IDs dos seus clientes. Para
  manter privado, renomeie sua cópia para `contas.local.yaml`, que já está no `.gitignore`.

Leia o [disclaimer no README principal](../README.md#disclaimer-use-com-responsabilidade) antes da
primeira escrita numa conta real.
