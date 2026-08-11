# Skills de Tráfego Pago para Claude Code

Duas skills que dão ao Claude Code controle das suas contas de anúncio pelas APIs oficiais, com
scripts Python que rodam na sua máquina, mais a base de conhecimento que ensina o Claude a **operar
como gestor**, não só a chamar endpoint.

Você conversa em português, ele opera o gerenciador:

- "lista as campanhas ativas do cliente X"
- "quanto gastei nos últimos 7 dias, quebrado por campanha"
- "cria uma campanha de leads com R$ 50 por dia"
- "quais termos de busca estão queimando verba sem converter?"
- "por que essa PMax não está gastando?"
- "esse pixel está saudável?"

| Skill | O que faz |
|---|---|
| [meta-ads/](meta-ads/) | Facebook e Instagram: 54 operações — leitura, métricas, segmentação, criação, edição, exclusão, duplicação e diagnóstico de pixel |
| [google-ads/](google-ads/) | Google: leitura e insights por GAQL, campanhas Search/PMax/Demand Gen, keywords, RSAs, extensões, negativas, Keyword Planner |
| [kb/](kb/) | a inteligência: método de otimização, métricas, criativo, e playbooks por modelo de negócio (e-commerce, negócio local, infoproduto) |

---

## Instalação

Você precisa de: Python 3, Claude Code, e acesso de administrador às contas que vai operar.

```bash
git clone <url-deste-repo> ~/skills-trafego-pago
cd ~/skills-trafego-pago
bash instalar.sh
```

O `instalar.sh` cria os links em `~/.claude/skills/`, instala os SDKs e prepara os `.env`. Como ele
usa link simbólico, atualizar o repo (`git pull`) atualiza as skills.

Se preferir na mão:

```bash
mkdir -p ~/.claude/skills
ln -s ~/skills-trafego-pago/meta-ads   ~/.claude/skills/meta-ads
ln -s ~/skills-trafego-pago/google-ads ~/.claude/skills/google-ads
ln -s ~/skills-trafego-pago/kb         ~/.claude/skills/kb
pip3 install facebook-business google-ads google-auth-oauthlib protobuf
```

**O link do `kb` não é opcional.** As duas skills consultam a base de conhecimento em `../kb/`; sem
ele, o Claude opera as contas mas perde a parte de estratégia. `kb` não é uma skill — o Claude Code
ignora pasta sem `SKILL.md`.

Depois abra o Claude Code e peça:

> "roda o setup da skill de meta ads"

ou

> "me ajuda a configurar a skill de google ads"

Ele conduz o resto: cria o app, gera o token, resolve o acesso às contas e cadastra seus clientes.
Se preferir fazer na mão, o passo a passo com as telas está em cada skill:

- Meta: [meta-ads/references/setup-meta-app.md](meta-ads/references/setup-meta-app.md)
- Google: [google-ads/references/setup-google-ads-api.md](google-ads/references/setup-google-ads-api.md)

**Comece pela Meta.** O setup dela leva 20 minutos; o do Google tem uma etapa de aprovação do
developer token que pode levar um dia.

### Conferir se ficou de pé

```bash
python3 ~/.claude/skills/meta-ads/scripts/read.py accounts
python3 ~/.claude/skills/google-ads/scripts/read.py accounts
```

Se os dois listarem suas contas, está pronto.

---

## Por onde começar a ler

| Arquivo | Para quê |
|---|---|
| [INSTRUCOES-CLAUDE.md](INSTRUCOES-CLAUDE.md) | **o briefing do Claude.** Como ele deve te conduzir, o que ler antes de agir, o que nunca fazer |
| [meta-ads/README.md](meta-ads/README.md) e [google-ads/README.md](google-ads/README.md) | o que cada skill faz |
| `*/aprendizados.md` | os erros reais. Cada entrada ali custou uma campanha rodando errada para alguém |
| [kb/README.md](kb/README.md) | o que tem em cada base de inteligência |

---

## Segurança

- Tokens ficam só nos arquivos `.env`, cobertos pelo `.gitignore`. Nada é enviado para lugar nenhum
  além das APIs da própria Meta e do próprio Google.
- **Toda criação nasce pausada.** Ativar exige a sua confirmação.
- Orçamento, exclusão e ativação sempre pedem confirmação antes.
- Se você preencher os `contas.yaml` com os IDs dos seus clientes e for versionar o repo, renomeie
  sua cópia para `contas.local.yaml` — já está no `.gitignore`.

---

## Disclaimer: use com responsabilidade

Estas skills foram construídas com Claude Code sobre a documentação oficial da
[Meta Marketing API](https://developers.facebook.com/docs/marketing-api/) e da
[Google Ads API](https://developers.google.com/google-ads/api/docs/start), e refinadas em operação
real de agência. Ainda assim:

- **Use por sua conta e risco.** Não há garantia de que o uso não resulte em restrição ou bloqueio
  nas suas contas de anúncio. As duas plataformas têm políticas próprias sobre automação e mudam as
  regras quando querem.
- **Leia as políticas.** [Termos de anúncios da Meta](https://www.facebook.com/policies/ads/),
  [rate limiting da Meta](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/)
  e [cotas do Google](https://developers.google.com/google-ads/api/docs/best-practices/quotas). As
  skills esperam entre operações de escrita, o que ajuda, mas não garante nada.
- **Revise o código.** As skills têm acesso de leitura e escrita às suas contas. Os scripts estão
  aqui justamente para serem lidos antes de usar.
- **Criação nasce pausada, mas edição e exclusão agem na hora.**
- **Sem garantia de funcionamento.** SDK e API mudam com frequência. O que funciona hoje pode
  quebrar amanhã, e quase sempre é mudança na API, não no seu setup.

Resumindo: é uma ferramenta poderosa, e a responsabilidade pelo que acontece na conta é sua. Não
faça por aqui nada que você não faria na mão no gerenciador.

---

## Créditos

O método operacional em `meta-ads/references/metodo-operacional.md` é a síntese da prática de quem
construiu estas skills. As bases em [kb/](kb/) são anotações destiladas do **Subido de Tráfego** e da
**Especialização de Tráfego**, do Pedro Sobral, e estão aqui como material de estudo entre alunos dos
cursos. Não substituem o curso: se o assunto interessa, o caminho é a fonte.
