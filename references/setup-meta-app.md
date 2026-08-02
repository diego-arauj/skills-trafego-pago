# Setup da Meta: app, token e acesso às contas

Guia do zero, para quem nunca criou um app na Meta. O Claude usa este arquivo para conduzir
o setup passo a passo. Se você travar em alguma tela, mande um print para ele e diga em que
etapa está.

Ordem: **criar o app → gerar o token → dar acesso às contas de anúncio → testar**. Pular a
terceira etapa é o erro mais comum: o token funciona, mas não enxerga nenhuma conta.

---

## Etapa 1 — Criar o app na Meta

1. Acesse [developers.facebook.com](https://developers.facebook.com/) e faça login com o
   Facebook que administra suas contas de anúncio.
2. Se for a primeira vez, aceite o cadastro de desenvolvedor (é gratuito).
3. **Meus Apps → Criar app**.
4. Em "caso de uso", escolha **Outro** e avance. Em tipo, escolha **Empresa** (Business).
5. Dê um nome qualquer (ex.: "Gestor de Anúncios") e associe a uma conta do Meta Business
   Manager se ele perguntar.
6. Dentro do app, **Adicionar produto → Marketing API → Configurar**.
7. Anote o **ID do app**: fica em **Configurações → Básico**. Ele vai no `META_APP_ID` do `.env`.

### O app precisa estar em modo Live

Em **Configurações → Básico** (ou no seletor no topo do painel) troque de **Desenvolvimento**
para **Ao vivo / Live**.

Em modo Desenvolvimento a leitura funciona, mas criar criativos e dark posts falha com "app em
modo de desenvolvimento". Se você só vai ler métricas, pode deixar como está; para criar
qualquer coisa, mude para Live.

---

## Etapa 2 — Gerar o token de acesso

Existem dois caminhos. Comece pelo primeiro; migre para o segundo quando a skill virar rotina.

### Caminho A — Token de usuário (rápido, para começar)

1. No painel do app: **Marketing API → Ferramentas** (ou acesse o
   [Graph API Explorer](https://developers.facebook.com/tools/explorer/)).
2. No topo direito, selecione o seu app.
3. Em **Permissões**, marque no mínimo:
   - `ads_read` — ler campanhas, anúncios e métricas
   - `ads_management` — criar, editar, pausar e excluir
   - `business_management` — enxergar as contas do Business Manager
   - `pages_show_list` e `pages_read_engagement` — necessárias para criar anúncios que usam
     uma página do Facebook
   - `instagram_basic` — para publicar no Instagram
4. Clique em **Gerar token de acesso** e autorize as telas do Facebook.
5. Copie o token.

**Esse token vale poucas horas.** Para estender para 60 dias, cole-o no
[Depurador de Token de Acesso](https://developers.facebook.com/tools/debug/accesstoken/),
clique em **Debug** e depois em **Estender token de acesso**. Copie o token longo resultante.

### Caminho B — System User (recomendado para uso contínuo)

Não expira sozinho e não quebra quando você troca a senha do Facebook.

1. Acesse [business.facebook.com/settings](https://business.facebook.com/settings).
2. **Usuários → Usuários do sistema → Adicionar**. Nome qualquer, função **Administrador**.
3. Selecione o usuário criado → **Adicionar ativos** → aba **Contas de anúncios** → marque as
   contas → permissão **Gerenciar campanhas** (controle total).
4. Repita em **Páginas** (permissão de gerenciar) e, se for anunciar no Instagram, em
   **Contas do Instagram**.
5. Ainda no usuário do sistema: **Gerar novo token** → escolha o app criado na Etapa 1 →
   marque `ads_management`, `ads_read`, `business_management`, `pages_show_list`,
   `pages_read_engagement`, `instagram_basic` → **Gerar token**.
6. **Copie na hora.** A Meta mostra o token uma única vez.

### Onde colocar

Copie `.env.example` para `.env` e preencha:

```
META_ADS_TOKEN="o token que você copiou"
META_APP_ID="o ID do app"
META_AD_ACCOUNT_ID="act_123456789"   # opcional
```

O `.env` está no `.gitignore`. Não cole o token em nenhum outro lugar, não mande por WhatsApp
e não cole numa conversa com o Claude: quem tem o token tem controle das suas contas.

---

## Etapa 3 — Dar acesso às contas de anúncio

Token válido não significa acesso às contas. Se `read.py accounts` volta vazio, é aqui que está
o problema.

### Se as contas são suas

Já pertencem ao seu Business Manager. Confirme em
[business.facebook.com/settings](https://business.facebook.com/settings) → **Contas de anúncios**
que você aparece com **Controle total**. Com token de System User, confirme que as contas foram
adicionadas como ativos dele (Etapa 2, item 3).

### Se as contas são de clientes

Peça ao cliente uma destas duas coisas. A primeira é a boa.

**Opção 1 (recomendada): parceria entre Business Managers.** O cliente entra no BM dele em
**Configurações → Parceiros → Adicionar parceiro**, informa o **ID do seu Business Manager**
(o seu, em Configurações → Informações da empresa) e concede acesso à conta de anúncios, à
página e ao perfil do Instagram, com permissão de **Gerenciar campanhas**.

A conta continua sendo do cliente. Se a parceria acabar, ele revoga o acesso e não perde nada,
e você não fica com o ativo dele preso no seu BM.

**Opção 2: acesso individual.** O cliente adiciona o seu e-mail pessoal como usuário da conta
de anúncios. Funciona, mas mistura tudo no seu perfil pessoal e é ruim de organizar quando você
tem vários clientes.

### O que precisa vir junto com a conta de anúncios

Só a conta de anúncios não basta para criar anúncios:

| Ativo | Para que serve | Sem ele |
|---|---|---|
| Conta de anúncios | tudo | nada funciona |
| Página do Facebook | identidade do anúncio | não cria criativo |
| Conta do Instagram | publicar no Instagram | "seu anúncio deve ser associado a uma conta do Instagram" |
| Pixel / dataset | otimizar por conversão e medir | não dá para usar `promoted_object` de conversão |

**Detalhe que confunde muita gente:** a página do Facebook e o perfil do Instagram **não
precisam estar vinculados entre si**. O que precisa é o Instagram estar vinculado à **conta de
anúncios** (Configurações do Negócio → conta de anúncios → Contas do Instagram). Se o perfil não
aparece como identidade no anúncio, é quase sempre esse vínculo que falta, e não o vínculo
página ↔ perfil.

### Conferindo

```bash
python3 scripts/read.py accounts
```

Tem que listar as contas. Se voltar vazio, revise a Etapa 3. Se der erro de permissão, revise as
permissões do token na Etapa 2.

---

## Etapa 4 — Instalar e testar

```bash
pip3 install facebook-business
python3 scripts/setup.py          # confere dependências e credenciais
python3 scripts/read.py accounts  # confere acesso
```

---

## Erros comuns e o que eles realmente significam

| Erro | Causa provável | Solução |
|---|---|---|
| `(#200) ads_management/ads_read` | conta não compartilhada com o seu BM, ou permissão faltando no token | Etapa 3, e revisar permissões na Etapa 2 |
| `(#10) Application does not have permission` | campo enviado no lugar errado (ex.: número de WhatsApp no criativo em vez do conjunto) | conferir onde o campo deve ficar, não é o app |
| `(#3) Application does not have the capability` | quase sempre payload incompleto, não permissão | ver `aprendizados.md`, entrada sobre criativo de post existente |
| `app em modo de desenvolvimento` | app não está Live | Etapa 1, final |
| `read.py accounts` volta vazio | token sem acesso a nenhuma conta | Etapa 3 |
| Erro 17, 32 ou 80004 | rate limit da API | esperar 60 segundos; app novo tem teto baixo |
| Token expirou em poucas horas | token curto do Explorer | estender no depurador, ou migrar para System User |

---

## Segurança

- O token dá controle das contas. Trate como senha de banco.
- Nunca versione o `.env`. O `.gitignore` já cobre isso, mas confira antes do primeiro commit.
- Se achar que vazou: **Business Manager → Usuários do sistema → o usuário → Revogar token**,
  ou troque a senha do Facebook (invalida tokens de usuário).
- Prefira System User a token pessoal: dá para revogar sem afetar seu login.
