# Meta Ads Skill para Claude Code

Skill que dá ao Claude Code controle das suas contas de Meta Ads (Facebook e Instagram) pela API
oficial da Meta, com scripts Python que rodam na sua máquina.

Você conversa em português, ele opera o gerenciador:

- "lista as campanhas ativas do cliente X"
- "quanto gastei nos últimos 7 dias, quebrado por campanha"
- "cria uma campanha de leads com R$ 50 por dia"
- "duplica essa campanha e troca as UTMs"
- "esse pixel está saudável?"

**54 operações** em 8 scripts: leitura, métricas, segmentação, criação, edição, exclusão,
duplicação e diagnóstico de pixel.

Mais do que os scripts, o que vem junto é o **conhecimento operacional**: um método de otimização
e um arquivo de erros e acertos que evita repetir enganos que já custaram campanha rodando errada.

---

## Instalação

Você precisa de: Python 3, Claude Code, e uma conta de anúncios da Meta com acesso de
administrador.

```bash
# 1. Clonar dentro das skills do Claude Code
git clone <url-deste-repo> ~/.claude/skills/meta-ads
cd ~/.claude/skills/meta-ads

# 2. Instalar o SDK da Meta
pip3 install facebook-business

# 3. Criar o arquivo de credenciais
cp .env.example .env

# 4. Abrir o Claude Code na pasta e pedir:
#    "roda o setup da skill de meta ads"
```

O Claude conduz o resto: cria o app na Meta, gera o token, resolve o acesso às contas e cadastra
seus clientes. Se preferir fazer na mão, o passo a passo completo com as telas da Meta está em
[references/setup-meta-app.md](references/setup-meta-app.md).

Para conferir se ficou tudo certo:

```bash
python3 scripts/setup.py
python3 scripts/read.py accounts
```

Se `accounts` listar suas contas, está pronto.

---

## O que tem aqui

| Arquivo | Para que serve |
|---|---|
| [INSTRUCOES-CLAUDE.md](INSTRUCOES-CLAUDE.md) | **Comece por aqui.** O briefing do Claude: como conduzir você, o que ler, o que nunca fazer |
| [SKILL.md](SKILL.md) | a skill: referência de todos os comandos e as regras de segurança |
| [aprendizados.md](aprendizados.md) | erros e acertos reais ao subir campanhas pela API, com os códigos de erro e o que eles significam de verdade |
| [references/setup-meta-app.md](references/setup-meta-app.md) | app, token, acesso às contas dos clientes, troubleshooting |
| [references/metodo-operacional.md](references/metodo-operacional.md) | o método: rotina de otimização, os seis parafusos, métricas, escala |
| [references/padroes-campanha.md](references/padroes-campanha.md) | configuração validada por tipo de campanha |
| [references/api-reference.md](references/api-reference.md) | referência de campos e endpoints |
| [contas.yaml](contas.yaml) | cadastro dos seus clientes: nome → IDs |
| `scripts/` | os scripts Python que falam com a API |

---

## Segurança

- O token fica só no `.env`, que está no `.gitignore`. Nada é enviado para lugar nenhum além da
  própria Meta.
- **Toda criação nasce pausada.** Ativar exige a sua confirmação.
- Orçamento, exclusão e ativação sempre pedem confirmação antes.
- Se você for versionar o `contas.yaml` preenchido, lembre que ele leva os IDs dos seus clientes.
  Para manter privado, renomeie sua cópia para `contas.local.yaml`, que já está no `.gitignore`.

---

## Disclaimer: use com responsabilidade

Esta skill foi construída com Claude Code a partir da documentação oficial do
[facebook-business SDK](https://github.com/facebook/facebook-python-business-sdk) e da
[Meta Marketing API](https://developers.facebook.com/docs/marketing-api/), e refinada em operação
real. Ainda assim:

- **Use por sua conta e risco.** Não há garantia de que o uso não resulte em restrição ou
  bloqueio na sua conta de anúncios. A Meta tem políticas próprias sobre automação e muda as
  regras quando quer.
- **Leia as políticas da Meta**, especialmente os [Termos de Serviço de anúncios](https://www.facebook.com/policies/ads/)
  e as [regras de rate limiting](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/).
  A skill inclui espera entre operações de escrita, o que ajuda mas não garante nada.
- **Revise o código.** A skill tem acesso de leitura e escrita às suas contas. Os scripts estão
  aqui justamente para serem lidos antes de usar.
- **Criação nasce pausada, mas edição e exclusão agem na hora.** Tenha cuidado.
- **Sem garantia de funcionamento.** O SDK e a API mudam com frequência. O que funciona hoje pode
  quebrar amanhã, e quase sempre é mudança na API, não no seu setup.

Resumindo: é uma ferramenta poderosa, e a responsabilidade pelo que acontece na sua conta é sua.
Não faça por aqui nada que você não faria na mão no Ads Manager.

---

## Créditos

O método de otimização em `references/metodo-operacional.md` é a síntese da prática de quem
construiu esta skill, apoiada no método ensinado pelo Pedro Sobral no Subido de Tráfego. Não é o
material do curso: se o assunto interessa, vale fazer o curso na fonte.
