# Setup da API do Google Ads, do zero

Este é o arquivo mais chato do repositório, e por um motivo: o Google exige **quatro peças
independentes** antes de a primeira consulta funcionar. Meta pede um app e um token; Google pede
conta MCC, developer token, projeto no Cloud e autorização OAuth. Se você já tentou e desistiu,
provavelmente parou na peça 2 ou na 5.

O mapa:

| # | Peça | Onde se resolve | Quanto demora |
|---|---|---|---|
| 1 | Conta MCC (administrador) | Google Ads | 5 min |
| 2 | Developer token | Central de API, dentro do MCC | 5 min + espera da aprovação |
| 3 | Projeto no Google Cloud com a Google Ads API ativada | Google Cloud Console | 5 min |
| 4 | Credencial OAuth (client id + secret) e refresh token | Cloud Console + `setup.py oauth` | 10 min |
| 5 | Acesso às contas dos clientes | Convite entre contas | depende do cliente |

Faça na ordem. A peça 2 depende da 1, e a 4 depende da 3.

---

## 1. Conta MCC (Minha Central de Clientes)

O MCC é a conta guarda-chuva que enxerga as contas dos seus clientes. **Você precisa de uma**, mesmo
que só opere a própria conta: o developer token só existe em MCC.

1. <https://ads.google.com/home/tools/manager-accounts/> → "Criar conta de administrador".
2. Use um e-mail que seja **só seu** (não o de um cliente). Essa conta vai ser a raiz de tudo.
3. Anote o ID dela, no canto superior direito, no formato `123-456-7890`. **Sem os hifens** ele vira
   o seu `GOOGLE_ADS_LOGIN_CUSTOMER_ID`.

Se você já opera clientes por um MCC, use o que já existe. Não crie outro.

---

## 2. Developer token

É a chave que autoriza *qualquer* chamada à API. Uma por MCC.

1. Entre no **MCC** (não numa conta de cliente).
2. Ferramentas e configurações → Configuração → **Central de API**
   (`Tools & Settings > Setup > API Center`).
3. Preencha o formulário e envie. Ele pergunta o que você vai fazer com a API: responda a verdade,
   em uma linha — gestão das contas dos meus clientes, leitura de relatórios e criação de campanhas,
   ferramenta interna, sem revenda.
4. O token aparece na hora, com o nível **"Acesso de teste"**.

### O detalhe que trava todo mundo

**Token de teste não funciona em conta real.** Ele só funciona em contas de teste do Google, que
não veiculam anúncio nenhum. Se você chamar a API numa conta de verdade com token de teste, o erro é:

```
DEVELOPER_TOKEN_NOT_APPROVED
```

Isso não é bug de configuração e não adianta mexer no OAuth. Você precisa pedir o **Acesso Básico**
na própria Central de API (botão "Solicitar acesso básico" / "Apply for Basic Access"). O formulário
pergunta o site da sua empresa, o que a ferramenta faz e como você lida com os dados. É análise
humana: costuma sair em algumas horas ou poucos dias.

Níveis, na prática:

| Nível | Serve para | Limite |
|---|---|---|
| Teste | só contas de teste | — |
| **Básico** | contas reais, é o que você quer | 15.000 operações/dia |
| Padrão | operações em volume alto | 1.000.000/dia |

**Enquanto o Básico não sai**, você não fica parado: faça as peças 3, 4 e 5. Quando o token for
aprovado, tudo já vai estar montado e a primeira chamada funciona.

---

## 3. Projeto no Google Cloud

O developer token diz *o que* pode ser feito. O OAuth diz *quem* está fazendo. Ele mora num projeto
do Google Cloud.

1. <https://console.cloud.google.com/> → criar projeto (nome livre, ex.: "ads-api").
2. Menu → APIs e serviços → **Biblioteca** → procurar **"Google Ads API"** → **Ativar**.
   - Se você pular esta ativação, a autorização até funciona, mas toda chamada volta com
     `PERMISSION_DENIED ... has not been used in project ... before or it is disabled`.
3. APIs e serviços → **Tela de permissão OAuth**:
   - Tipo de usuário: **Externo** (a menos que sua conta seja Workspace e você só vá usar você mesmo).
   - Preencha nome do app, e-mail de suporte e e-mail do desenvolvedor. O resto pode ficar em branco.
   - Em **Usuários de teste**, adicione o seu próprio e-mail do Google Ads. Sem isso, a autorização
     do passo 4 recusa com "acesso bloqueado".
   - **Não precisa publicar nem passar por verificação** para uso próprio. App em modo de teste
     funciona; a única consequência é que o refresh token pode expirar a cada 7 dias. Se isso te
     incomodar, publique o app (botão "Publicar", status "Em produção") — para uso interno o Google
     não exige verificação, ele só mostra um aviso de "app não verificado" na tela de autorização,
     e você clica em "Avançado > Acessar mesmo assim".

---

## 4. Credencial OAuth e refresh token

1. Cloud Console → APIs e serviços → **Credenciais** → Criar credenciais → **ID do cliente OAuth**.
2. Tipo de aplicativo: **App para computador** (Desktop app). Esse tipo importa: ele libera o
   redirect local que o `setup.py` usa. Se você escolher "Aplicativo da Web", o fluxo quebra com
   `redirect_uri_mismatch`.
3. Copie o **ID do cliente** e a **Chave secreta** para o `.env`:

```
GOOGLE_ADS_CLIENT_ID="....apps.googleusercontent.com"
GOOGLE_ADS_CLIENT_SECRET="..."
GOOGLE_ADS_DEVELOPER_TOKEN="..."
GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"
```

4. Gere o refresh token:

```bash
python3 scripts/setup.py oauth
```

Abre o navegador, você autoriza **com a conta Google que tem acesso ao MCC**, e o script grava o
`GOOGLE_ADS_REFRESH_TOKEN` no `.env` sozinho. Você não copia nem cola nada.

5. Teste:

```bash
python3 scripts/setup.py test     # lista as contas que você alcança
python3 scripts/read.py accounts
```

Se listou as contas, as quatro peças estão no lugar.

### Se der errado aqui

| Erro | O que é de verdade |
|---|---|
| `DEVELOPER_TOKEN_NOT_APPROVED` | token ainda em Teste (peça 2). Não é OAuth. |
| `redirect_uri_mismatch` | a credencial foi criada como "Aplicativo da Web". Recrie como "App para computador". |
| `acesso bloqueado: o app não concluiu a verificação` | seu e-mail não está em "Usuários de teste" na tela de permissão OAuth. |
| `PERMISSION_DENIED ... API has not been used in project` | faltou ativar a Google Ads API na Biblioteca (peça 3). |
| `USER_PERMISSION_DENIED` | a conta que autorizou não tem acesso àquele customer_id. É a peça 5. |
| `CUSTOMER_NOT_ENABLED` | conta suspensa, encerrada ou sem forma de pagamento. Nada a ver com a API. |
| trava sem erro nenhum, no macOS | `GRPC_DNS_RESOLVER=native` na frente do comando. Ver `aprendizados.md`. |

---

## 5. Acesso às contas dos clientes

Credencial válida não dá acesso a conta nenhuma. Esta é a etapa que mais atrasa o setup, porque
depende de outra pessoa clicar em algo.

**O caminho certo: vincular a conta do cliente ao seu MCC.**

1. No seu MCC: **Contas → Mais (+) → Vincular conta existente**.
2. Digite o ID da conta do cliente (`123-456-7890`).
3. O cliente recebe um convite dentro da conta dele (sino de notificações, e por e-mail para os
   administradores). Ele precisa **aceitar**.
4. Depois de aceito, a conta aparece no seu `read.py accounts`.

O que dizer ao cliente, porque a pergunta sempre vem: **a conta continua sendo dele**. Vincular ao
MCC de uma agência dá acesso de gestão, não transfere propriedade, e ele pode remover o vínculo
quando quiser. A cobrança continua no cartão dele, na conta dele.

**Nível de acesso.** Peça acesso de **Administrador** se você vai criar e editar campanhas. "Somente
leitura" e "Padrão" bloqueiam parte das operações de escrita, e o erro que aparece é um genérico de
permissão, que parece problema de token.

**Se o cliente já está em outro MCC** (de outra agência), a conta pode ser vinculada a mais de um
gerenciador — não precisa desvincular do anterior.

**Alternativa sem MCC:** o cliente adiciona o seu e-mail direto como usuário administrador da conta
dele (Administrador → Acesso e segurança → convidar). Funciona, mas dá trabalho: sem MCC você
autoriza o OAuth com um e-mail que enxerga aquela conta e o `LOGIN_CUSTOMER_ID` passa a ser a própria
conta. Com muitos clientes vira bagunça. Use o MCC.

---

## 6. Vários clientes com credenciais separadas

Às vezes um cliente exige que você opere com o developer token dele (MCC próprio, política interna).
Nesse caso, crie um `.env.<perfil>` ao lado do `.env`:

```
.env             # padrão
.env.clientex    # credenciais do cliente X
```

e chame os scripts com o perfil:

```bash
GOOGLE_ADS_ENV=clientex python3 scripts/read.py campaigns --customer-id 9876543210
```

No `contas.yaml`, marque o cliente com `env_profile: "clientex"` para o Claude saber qual usar sem
você precisar lembrar.

---

## 7. Checklist final

```bash
python3 scripts/setup.py check    # o que falta no .env
python3 scripts/setup.py test     # a conexão funciona?
python3 scripts/read.py accounts  # quais contas eu alcanço?
python3 scripts/read.py campaigns --customer-id <id>
```

Se `accounts` lista as contas e `campaigns` traz as campanhas de uma delas, está pronto para operar.

---

## Documentação oficial

- Primeiros passos: <https://developers.google.com/google-ads/api/docs/get-started/introduction>
- Developer token e níveis de acesso: <https://developers.google.com/google-ads/api/docs/access-levels>
- OAuth (desktop app): <https://developers.google.com/google-ads/api/docs/oauth/installed-app>
- Limites e cotas: <https://developers.google.com/google-ads/api/docs/best-practices/quotas>
- Referência de GAQL: <https://developers.google.com/google-ads/api/docs/query/overview>
