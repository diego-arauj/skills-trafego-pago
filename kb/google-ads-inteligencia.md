# Google Ads, base de inteligência (Curso Subido de Tráfego)

> O método universal de otimização, métricas, criativos e contingência está em `meta-ads-inteligencia.md` (mesma pasta). Este arquivo cobre apenas o que é específico do Google Ads.

---

## 1. Como funciona o Google Ads e o leilão

- Não ter medo do Google Ads: é o mesmo "idioma" do tráfego pago que já se domina na Meta. Os botões são praticamente iguais e a lógica difícil já foi aprendida.
- Diferença de superfície: Meta tem muitos posicionamentos dentro de POUCOS aplicativos (Instagram/Facebook: explorar, stories, feed, Reels). Google tem anúncios em MUITOS locais diferentes (vídeo no YouTube, e-mail no Gmail, pesquisa, sites/apps parceiros, Maps, Discover, Shopping).
- Atenção vs intenção: Meta é muito mais ferramenta de ATENÇÃO e relação (a pessoa não procura seu produto). Google é muito mais INTENÇÃO (aparece na frente da busca/intenção de compra, ex.: alguém pesquisando "batedeira elétrica industrial"), além de atenção e relação no YouTube. Mundo ideal = anunciar nos dois.

### O leilão (3 fatores, igual à Meta)
- O leilão decide qual anúncio aparece e qual não. Não é só dinheiro: mesmo com dinheiro infinito não se ganha tudo.
- Os 3 fatores que definem quem ganha:
  1. Lance: quanto se está disposto a pagar por um resultado.
  2. Taxa de ação estimada: probabilidade de a pessoa da segmentação realizar o objetivo (relação segmentação x objetivo).
  3. Qualidade do anúncio.
- No Google esse mecanismo se formaliza no Índice de Qualidade (ver seção 11, MOIQ): o Google atribui nota a relevância, CTR esperado e experiência na página, MULTIPLICA pelo lance e gera a nota que define a posição. Mito derrubado: pagar mais para aparecer primeiro não funciona; dá para aparecer na frente de um concorrente pagando metade ou menos do clique dele.

### Conexões que o Google Ads exige
- YouTube: anúncios em vídeo e remarketing de quem interagiu com o canal. Mesmo sem nada publicado, é preciso subir os vídeos em modo NÃO LISTADO para poder anunciá-los (vídeo não listado não aparece para quem entra no canal, serve só para anúncios).
- Google Analytics (GA4): ações do usuário no site e segmentações.
- Google Merchant Center: e-commerce, puxa imagens da loja para anúncios automatizados.
- Google Business Profile / Google Meu Negócio: negócio local/loja física.
- Aprofundamento técnico (Analytics, Merchant, Tag Manager) deve ser objetivo: dominar o que a ferramenta oferece para gerar resultado, sem virar especialista de 30 a 40h.

### Redes do Google (locais de anúncio)
- Rede de Pesquisa (Search): anúncio na frente da busca/intenção. 100% dos anunciantes deveriam anunciar na pesquisa, no mínimo para o próprio nome/marca (garantir que aparece quando pesquisam por você).
- Rede de Display (GDN): espaços publicitários em sites/blogs parceiros; cerca de 9 em cada 10 sites vendem espaço ao Google (alcance quase total). Melhor uso: REMARKETING.
- YouTube: muito versátil; serve para impressão/reconhecimento, consideração/relação e conversão/venda.
- Outras: Google Shopping (junto à pesquisa), Google Maps, anúncios em aplicativos, Gmail e Discover.

### Estrutura da conta (3 níveis, igual à Meta)
- Campanha: define objetivo, tipo de campanha, orçamento e configurações gerais. No Google a MAIOR parte das configurações fica na campanha (datas de início/fim etc.). Na Meta isso fica no grupo de anúncio.
- Grupo de anúncio: define lances e segmentação. No Google o lance é configurado aqui (salvo estratégia automática); na Meta o lance é atrelado ao orçamento.
- Anúncio: define o anúncio (títulos/descrições no Search), as extensões de anúncio (recursos extras, "cereja do bolo", deixam mais clicável) e o destino.

### Objetivos de campanha
- Vendas; Leads; Tráfego no site; Reconhecimento e consideração (une o "reconhecimento" e o "engajamento" da Meta); Promoção do aplicativo; Visitas a lojas locais e promoções (exige Google Business Profile bem configurado); Campanha sem meta (uso raro, às vezes para recursos beta).

### Tipos de campanha
- Pesquisa (mais clássico).
- Performance Max / PMax (mais automatizada, análoga à Advantage da Meta, menos opções de configuração).
- Geração de demanda / Demand Gen (aparece em vários lugares; hoje abriga as campanhas de conversão de vídeo do YouTube para vendas).
- Display (sites parceiros).
- Shopping (e-commerce no Google Shopping).
- Vídeo (YouTube).
- Aplicativo (divulgação de apps).

---

## 2. Estrutura de conta: criação, acesso e configuração

### Criar uma conta de anúncios
- Acessar via busca "Google Ads" (opção "conquiste clientes e venda mais com anúncios") ou business.google.com/br/google-ads. Acessar conta ou "começar agora".
- Antes de prosseguir, resgatar oferta de créditos: "escolher uma oferta". Mecânica: para receber o crédito é preciso investir o mesmo valor da oferta no prazo (ex.: oferta R$200 = investir R$200 nos primeiros 60 dias). Recomendado a iniciantes a oferta de R$200 (há também gastar R$1.200 e ganhar R$1.200; oferta de R$2.500 exige investir R$2.500). Clicar "clique para resgatar".
- O sistema empurra a criação de campanha; NÃO criar campanha agora. Preencher uma URL qualquer, avançar, avançar, e na parte inferior escolher "não quer criar uma campanha? Configure apenas a conta".
- Definir país, fuso horário e moeda (Brasil, horário de Brasília, Real Brasileiro).
- Criar perfil de pagamentos: forma de pagamento, organização (CNPJ) ou pessoa física (CPF + data de nascimento), endereço (CEP, número, bairro, estado, parte autopreenchida).
- Forma de pagamento: cartão de crédito/débito, Pix ou Mercado Pago. Salvar cartão.
- Se for agência de tráfego, marcar "sim" para "sua organização é uma agência de publicidade" e informar o que deseja verificar (dados da agência ou do cliente).

### Nomear a conta e configurar a tag
- Nomear a conta: Admin > Configurações da conta > definir nome > salvar (senão só aparece o código da conta).
- Tag do Google: Ferramentas > Central de dados > Tag do Google > Gerenciar. Instalação por criador de sites (parceiros) ou manual (copiar a tag). Recomendado: manual via Google Tag Manager. A tag principal deve estar em TODAS as páginas.
- Vincular YouTube: Vincular canal > pesquisar pelo nome > selecionar > avançar. O e-mail informado precisa ser exatamente o vinculado ao canal; aceitar a solicitação no e-mail. Status vai de "enviado" para "vinculado".
- Vincular Google Analytics: usar e-mail com propriedades no Analytics, selecionar a propriedade, manter ativado, vincular.

### Como o cliente concede acesso ao Google Ads
- Menu lateral esquerdo: Admin > Acesso e segurança. Três abas: Usuários, Administradores, Segurança.
- Adicionar pessoa: ícone "+", inserir e-mail. Data de expiração: normalmente "nunca" (dá para remover depois). Nível de acesso: para gerenciar a conta toda, Administrador; para limitar, outra opção. Enviar convite.
- Autenticação de dois fatores: pegar código no e-mail e confirmar. Se aparecer mensagem de erro, clicar de novo em enviar convite. O convite fica pendente até a pessoa aceitar pelo e-mail; depois aparece em Administradores.
- Erro "Este endereço não está em um domínio permitido" (ao convidar e-mail de domínio empresarial, ex.: @subido.com.br): Segurança > Domínios permitidos > Adicionar domínio (ex.: subido.com.br) > salvar. Depois o convite funciona.
- Dois administradores nas contas do Google é praticamente obrigatório: se um perfil for bloqueado, o outro segue mexendo nas campanhas.

---

## 3. Rede de pesquisa e palavras-chave

### Lógica do "bolo de cenoura fofinho"
- O que a pessoa PESQUISA (termo de pesquisa) = o RESULTADO da pesquisa = a PÁGINA de destino. Esses 3 têm que se conectar. Você controla: termo via PALAVRA-CHAVE, resultado via ANÚNCIO, destino via LANDING PAGE. Conectar o triângulo domina o leilão, aparece no topo e gera resultado.
- Estrutura: CAMPANHA > GRUPOS DE ANÚNCIO. Olhe cada grupo de anúncio como um GRUPO DE PALAVRAS-CHAVE de uma mesma categoria/tema. Pode haver 6 a 12+ grupos. Em cada grupo, só anúncios relacionados àquele tema (pesquisou "tráfego pago" vê anúncio de tráfego pago).

### 11 boas práticas para os anúncios de pesquisa
1. Respeitar a lógica do bolo de cenoura (grupo foca numa palavra específica, anúncio foca nela).
2. Usar o MÁXIMO de recursos do Google (até 15 títulos, 4 descrições, extensões, logo, imagem).
3. Analisar TODOS os anúncios da concorrência (gastar 20 a 40 min pesquisando os termos e pensando como fazer melhor; ninguém faz isso).
4. Usar call to actions em algum título (clique aqui, saiba mais, se cadastre agora, garanta).
5. Destacar BENEFÍCIOS em alguns títulos (o que a pessoa ganha), ligado ao ICP.
6. Incluir o NOME DA MARCA nos anúncios (ajuda branding e conversão).
7. Incluir BÔNUS se fizer sentido (às vezes a pessoa clica pelo bônus).
8. Especificar o TEMPO da ação no site ("sua compra em menos de 2 minutos").
9. REPETIR as palavras-chave nas descrições e títulos (reforça a lógica do bolo).
10. Fazer PERGUNTAS na copy ("está procurando por [X]?").
11. Usar parâmetros dinâmicos.

### 3 tipos de parâmetros dinâmicos
- Inserção de palavra-chave: `{keyword:Pedro Sobral}`, substitui o título pela pesquisa da pessoa; se a pesquisa for longa demais ou violar políticas, usa o texto padrão ("Pedro Sobral"). É o melhor para a lógica do bolo de cenoura. SEMPRE usar.
- Countdown: `{countdown}`, contagem regressiva para um evento (o Google abre pop-up para definir o tempo).
- Inserção de local: `{location}`, mostra cidade/estado/país conforme onde a pessoa está ("Contrate gestor de tráfego em [Nova York]"). Ótimo para várias localizações.

### Lista de palavras-chave
- Boa lista serve para dois fins: bons anúncios na rede de pesquisa E criar segmentos personalizados (públicos de quem já fez buscas / tem interesses). Um dos maiores diferenciais do anunciante no Google.
- Palavra-chave vs termo de pesquisa: palavra-chave é o que VOCÊ diz ao Google que quer anunciar (a isca que você escolhe); termo de pesquisa é o que a pessoa EFETIVAMENTE digitou (o peixe que mordeu, às vezes exato, às vezes inesperado). A palavra-chave dá dicas/direção ao Google.

Passos para montar a lista:
- Passo 1: saber com quem você fala (módulo de ICP/persona, hoje feito com IA).
- Passo 2: ter palavras-chave positivas e negativas PADRÃO da conta. Tão importante saber para quem aparecer quanto para quem NÃO aparecer.
  - Positivas padrão (intenção de compra): comprar, pedir, contratar, orçamento, adquirir, encomendar.
  - Negativas padrão (não-intenção): barato, "faça você mesmo"/"do it yourself", gratuito, por conta própria, grátis.
  - Dever de casa: listar as palavras do seu negócio que expressam (e que não expressam) intenção de compra; varia por negócio. O material extra traz lista gigante de negativas com microvariações, mas não copiar tudo: ler e escolher o que faz sentido.
- Passo 3: encontrar a lista das melhores palavras-chave, por 6 fontes:
  1. O cérebro: calçar os sapatos do cliente. Começar pelas palavras da MARCA (último nível de consciência, busca pelo nome do negócio; ex.: "comunidade subido", "Pedro Sobral"), depois palavras com intenção de compra do produto (ex.: "comprar curso de tráfego pago", não "curso de tráfego gratuito").
  2. Planejador de palavras-chave do Google: mostra volume de pesquisas/mês (média) e a competição/quanto pagar no lance para aparecer na primeira posição.
  3. Ferramentas externas: AnswerThePublic (adquirida por Neil Patel), muito boa; definir o país e no máximo dois termos por consulta (ex.: usar "tráfego pago", não "comprar curso de tráfego pago"); retorna dezenas a centenas de buscas relacionadas.
  4. "Roubar como um artista": pesquisar no Google e YouTube as palavras já mapeadas e observar (a) o que está escrito nos anúncios e (b) os resultados ORGÂNICOS (ignorados pela maioria, mas são o maior indicativo de quais palavras funcionam: se o título orgânico tem uma palavra-chave é porque atrai cliques). Títulos do YouTube cumprem o mesmo papel.
  5. Inteligências artificiais: jogar a pesquisa de audiência numa IA e pedir ideias de palavras-chave com intenção de compra. Há agentes específicos (persona, anúncios, conteúdos, ganchos, anúncios de rede de pesquisa, ideias de palavras-chave).
  6. Termos de pesquisa: o próprio Google informa os termos que ATIVARAM seus anúncios; minoria analisa (dá trabalho). Sentar 30 minutos a cada 15 dias analisando termos entrega tudo que precisa para otimizar.
- Organização: colocar a lista no Excel separando por CATEGORIAS/temas (facilita muito a criação das campanhas).
- Passo 4: escolher a correspondência de palavra-chave (3 tipos, diferenciados pelo sinal ortográfico):
  - Ampla (sem sinal, ex.: doces saudáveis em cidade X): aparece para termos RELACIONADOS/parecidos. Vantagem: aparece para bons termos não pensados; risco: aparece para termos ruins não antecipados (exige cuidado na análise dos termos).
  - Frase (entre "aspas"): aparece quando a pesquisa CONTÉM aqueles termos naquela ORDEM, podendo ter palavras antes/depois. Não aparece se quebrar a ordem/termo.
  - Exata (entre [colchetes]): aparece SÓ para o termo digitado; limita, não dá ideia de tudo que as pessoas pesquisam.
  - Recomendação ao começar: usar principalmente FRASE (aspas) e EXATA (colchetes) juntas; ampla pode, mas com muito cuidado nos termos que ativam as buscas.
- O Google ignora erro de digitação, acentuação, maiúsculas/minúsculas (entende a intenção); NÃO criar variações com erros de digitação (desperdício).
- Passo 5: colocar as palavras na planilha de correspondência (material extra); ao escolher o tipo (frase/exata), a planilha insere automaticamente aspas/colchetes.

### Criar campanhas de pesquisa (duplicar grupos e anúncios)
- Duplicar grupo de anúncios: clicar no nome da campanha (abre a área de grupos) > selecionar o grupo > copiar (Ctrl+C / Ctrl+V no Windows ou Editar > Copiar / Colar) > escolher a campanha de destino (vem pré-selecionada a atual) > Concluído e Colar.
- Opção "pausar grupos novos depois de colar": manter desativada se não quiser o grupo pausado.
- Grupo duplicado aparece em negrito e com hashtag (#) ao lado do nome; processo rápido, pode rodar em segundo plano. Depois ajustar nome e alterações.
- Duplicar anúncio: entrar no grupo > barra lateral (Campanhas) > Anúncios > selecionar o anúncio > Editar > Copiar > Colar > escolher campanha e grupo de destino > Concluir.
- Ao colar anúncio surge a opção extra "se já existe um anúncio no destino, cria um anúncio duplicado": recomendado manter ATIVADA, senão o sistema pode impedir a duplicação de anúncio idêntico.
- Anúncio duplicado aparece em negrito com status "pendente / em análise" (sem hashtag, diferente do grupo). Depois de duplicar, editar (títulos, recursos) e Salvar (não manter dois anúncios idênticos).

---

## 4. Segmentações no Google Ads

### 4 maneiras de segmentar
1. Público alvo (características das pessoas).
2. Conteúdo (que conteúdo a pessoa está assistindo/pesquisando/acessando: o vídeo, site, pesquisa, assunto, palavra-chave do conteúdo, não a característica da pessoa).
3. Segmentação otimizada (o Google escolhe; EVITAR ao máximo porque o Google não manda bem, mas é teste válido pois o que não funcionava pode funcionar hoje).
4. Indicadores de público alvo (usados em Performance Max: não se define para quem aparecer, dá-se uma sugestão e o Google encontra o público).

### Segmentação de PÚBLICO ALVO (4 sub-tipos)
- (a) Seus dados (remarketing): visitantes do site, usuários de app, quem interagiu com o YouTube, listas de clientes, e públicos criados via Google Analytics (essencialmente igual a visitantes do site).
- (b) Segmentos personalizados (favoritos): baseados em intenção de compra (lista de palavras-chave relacionadas à intenção); baseados em pesquisas de termos no Google (anunciar para quem JÁ fez aquela busca alguma vez na vida, não no momento da busca; um dos melhores públicos do Google); baseados em sites (colocar sites de concorrentes, canais/vídeos do YouTube, funciona muito bem); baseados em aplicativos (anunciar para quem tem apps específicos no celular, funciona muito bem).
- (c) Interesses e informações demográficas ("listas prontas", disponíveis a você e a todos os concorrentes): No mercado / in-market (intenção de compra em assuntos, ir nos mais óbvios); Eventos importantes (mudou de emprego, adotou cachorro, trocou de casa); Informações demográficas detalhadas (idade do filho, faturamento mensal); Afinidade (afinidades com temas).
- (d) Dados demográficos (usados em 100% das campanhas): idade, gênero, localização, renda. Renda funciona diferente por país: muito precisa nos EUA, pior em países latino-americanos/espanhóis, pior ainda na Europa (lei de proteção de dados limita o uso das informações).

### Segmentação de CONTEÚDO (3 tipos)
- (a) Canais, vídeos e sites (escolher canais/vídeos do YouTube ou sites específicos onde aparecer).
- (b) Temas (lista pronta de assuntos; antes "tópicos"; usar muito pouco por falta de resultado).
- (c) Palavras-chave (a estrela do Google Ads; única ferramenta de anúncio com muita inteligência em palavra-chave). Usar para tudo: segmentação de conteúdo E público de segmento personalizado de quem já fez buscas. Boa lista bem curada é uma das tarefas mais importantes do anunciante no Google.

### Criar públicos (prática)
- Acesso: Ferramentas > biblioteca compartilhada > gerenciador de públicos-alvo > "Públicos-alvo" (topo) > ícone de mais. Ideia: deixar a segmentação estruturada antes de criar a campanha.
- Criar segmento personalizado: "criar novo segmento" > "pessoas com qualquer um destes interesses ou intenções de compra" > adicionar palavras-chave (interesses/intenções) ou termos pesquisados no Google (ex.: tráfego pago, marketing digital, gestor de tráfego pago).
- IMPORTANTE: segmentar por sites específicos (ex.: universosubido.com.br) atinge sites SEMELHANTES, não exatamente aquele domínio. Idem para apps semelhantes. Nomear o segmento e salvar.
- Outros tipos: remarketing (curtiram vídeos, visitaram site, interagiram com YouTube); interesses (com especificação, ex.: mobiliário doméstico); eventos importantes (casamento, formatura, nascimento de filho, mudança de emprego); informações demográficas (estado civil, escolaridade, status de moradia proprietário/inquilino, setor de atuação, tamanho da empresa); afinidade.
- É possível EXCLUIR públicos: ex.: excluir lista de clientes que já compraram e anunciar só para homens 25-54, renda 10% a 50%, excluindo a categoria "desconhecida". Dar nome e salvar.

---

## 5. Performance Max (PMax)

- O que é: campanha que aparece em TODAS as redes do Google Ads (YouTube, rede de display, pesquisa, Discover, Gmail, Maps). Se o Google lançar nova rede, a PMax automaticamente passa a aparecer lá. Proposta "one fits all".
- Nomenclatura de estrutura diferente: no Google padrão há campanhas > grupos de anúncio > anúncios. Na PMax há campanhas > "indicadores de público-alvo" (equivale a grupo de anúncio) > "grupos de recursos" (equivale a anúncios).
- Indicador de público-alvo: em vez de mandar o Google anunciar para um público fixo, você dá uma SUGESTÃO de público (análogo a público com sugestão da Meta). Aceita segmentação de público-alvo E de conteúdo.
- Grupos de recursos: você entrega "munição" (formatos) para o Google montar os anúncios: imagens, vídeo, texto. Para visitas a lojas locais, entregar um Google Business Profile bem estruturado (de onde puxa imagens, títulos, categorias). Como aparece em todas as redes, precisa de títulos/descrições (pesquisa), vídeos (YouTube) e imagens (display).
- Boa prática central: usar seus melhores anúncios e públicos VALIDADOS nas outras redes como base. O sucesso da PMax depende de ter tido tempo de testar e validar recursos e públicos antes (pesquisa: keywords e anúncios; YouTube: públicos e anúncios; display: banners/imagens).
- Cuidado com qualidade: PMax entrega muita ESCALA, mas pode entregar com péssima qualidade, principalmente fora de campanha de venda. Em campanha de cadastro/leads sem avaliar qualidade, você compra leads baratos porém ruins. Solução: lead scoring (avaliação automatizada ou pesquisa com perguntas-chave pós-cadastro). Em campanha de vendas o problema é menor (vê logo se converte).
- Visitas a lojas locais: o objetivo "visitas a lojas locais" SÓ permite o tipo PMax. Exige Google Business Profile bem configurado.
- PMax para e-commerce: sempre funciona muito bem.

### Melhores práticas PMax
1. Usar seus melhores anúncios (descobertos em outras campanhas) no grupo de recursos.
2. Testar diferentes grupos de recursos em diferentes campanhas. Se tem 15 títulos, testa 30; se tem 5 vídeos, testa 10.
3. Colocar de 2 a 4 grupos de recurso por campanha. Atenção: com vários grupos numa mesma campanha, a PMax NÃO reporta o resultado individual de cada grupo. Para comparar grupos, usar campanhas distintas.
4. Criar indicador de público de duas formas: (a) focar no público que você BUSCA, ex.: para captar novos clientes, entregar a lista de clientes atuais como indicador (o Google busca perfis parecidos, funciona muito bem); (b) focar num público muito QUENTE já validado. Caso real: em captação de leads, indicar a lista de leads já captados performou melhor que indicar público quente, e paga mais barato.
5. Fazer a segmentação demográfica o melhor possível para qualificar (ex.: se 70% dos clientes têm certa idade, focar nela).
6. Na localização, testar localizações mais premium (público de maior poder aquisitivo) para qualificar.
- Lógica suprema: sempre buscar maneiras de QUALIFICAR as pessoas que vêm da PMax.

### Criar PMax de captação de leads (prática)
- Caminho: ícone colorido de mais > Campanha > objetivo "Leads".
- Manter apenas UMA meta de conversão ativa (remover as demais); para leads, costuma ser "Contatos".
- Tipo: Performance Max. Informar URL de destino. Nomenclatura clara (ex.: "Performance Max Leads").
- Lances: foco em conversões; CPA-alvo opcional (inserir valor ou deixar otimizar). Começar com Conversões e migrar para CPA depois.
- Locais: adicionar local específico (ex.: Brasil). Idioma: manter todos.
- Programação de anúncios: configurar os 7 dias individualmente (facilita ajustes/análise futura), mesmo parecendo igual a "todos os dias".
- Dispositivos: avaliar excluir "telas de TV".
- Opção "expansão de URL" (enviar tráfego para as páginas mais relevantes do site): desnecessária quando o destino é só uma landing page; útil em e-commerce.
- Grupo de recursos: nomenclatura (ex.: "institucional"); nome da empresa; até 5 logotipos em formatos variados (inclusive quadrado); preencher todos os títulos, títulos longos e descrições; imagens estratégicas e vídeos (vídeos publicados no YouTube, inserir link).
- Sitelinks: adicionar variações. Se usar landing page, NÃO repetir exatamente a mesma URL (gera erro de duplicação); alternativa: copiar link de uma âncora interna da própria página (mesmo destino, URL diferente).
- Call to action (ex.: "Saiba mais") + frases de destaque + mais recursos.
- Temas de pesquisa: adicionar termos relacionados à marca (amplia alcance com coerência).
- Indicador de público-alvo: selecionar públicos já criados (visitantes do site, usuários do YouTube, lista de clientes) e/ou interesses. Ajustar gênero, idade, renda. Se aparecerem leads desqualificados, revisar essas configurações.
- Orçamento: ex.: R$50. O sistema revisa e pode apontar pendências (ex.: falta de logotipo); ajustar e publicar.

---

## 6. Display (GDN)

- Definição: campanhas de Display = campanhas de remarketing/retargeting: aparecer de novo para quem já teve contato (visitou o site, quase converteu). Analogia: "ser perseguido por geladeiras na internet".
- GDN: cerca de 90% dos sites da internet vendem espaço ao Google, dando alcance gigante.
- Ônus e bônus do alcance gigante: bônus = aparecer para quase todo mundo; ônus = público desqualificado, principalmente para público FRIO. Caso real (professor de inglês): banners apareciam em sites de vagas e as pessoas confundiam o banner com o conteúdo. Segmentação de conteúdo ajuda na teoria mas não resolve na prática para frio (rede grande demais).
- Solução: fazer Display focado em públicos QUENTES (usar o bônus do alcance escolhendo gente qualificada). Não anunciar para quem não conhece a marca em Display (pode até sujar a marca).

### 3 tipos de campanha que funcionam na GDN (todos remarketing/público quente)
1. Remarketing para vendas e leads (foco performance): quem quase comprou/quase se cadastrou.
2. Remarketing para lembrete (foco performance): lembrar de promoção, novidade, novo produto, aula ao vivo hoje 20h.
3. Remarketing para branding (NÃO é performance): só aparecer de novo e de novo (ser a "Coca-Cola da internet"), usando objetivo de reconhecimento/consideração; pouco usado, mas funciona bem.

### Lances por objetivo (Display)
- CPA desejado para campanhas focadas em vendas.
- CPC desejado ou otimizado (testar) para tráfego no site/lembrete.
- CPM para campanhas focadas em imprimir.
- Dica de múltiplas campanhas (quando há verba sobrando e se quer cobrir todo o público): criar duas ou três campanhas separadas, uma CPM, uma CPC, uma CPA. CPM encontra pessoas propensas a só ver; CPC, propensas a clicar (perfis diferentes). Para a maioria, escolher um único objetivo.

### Anúncios/formatos e otimização (Display)
- Não decorar tamanhos de banner; usar o "guia de formatos da rede de display" (material extra) e passar ao designer. Regra básica: usar TODOS os formatos possíveis (designers produzem o mesmo banner em dezenas de tamanhos facilmente). Não ter um formato (ex.: 300x300) impede aparecer em sites que só têm aquele espaço.
- Otimização: usar a aba "onde os anúncios foram exibidos" para ver em quais sites aparece, acessá-los e excluir os que não geram resultado ou têm CPM caro. Se a qualidade estiver ruim, segmentar por palavras-chave que devem estar nos sites OU testar segmentação por temas/tópicos. CUIDADO: essas restrições podem (1) não funcionar e (2) matar a escala (Display precisa de volume de sites diferentes).

### Criar Display (prática)
- Caminho: Campanhas > ícone de mais > escolher objetivo (ex.: Vendas).
- Regra de meta de conversão: escolher APENAS UMA por campanha; remover as demais (três pontos > Remover > confirmar). Múltiplas metas atrapalham a leitura dos dados.
- Tipo: Rede de Display. Inserir o site de destino (URL final). Nomenclatura clara (ex.: "RD vendas remarketing").
- Para remarketing: manter "todos os países e territórios" e "todos os idiomas" faz sentido (público já interagiu e é menor). Para público frio, definir localização e idioma específicos.
- Programação de anúncios: NÃO deixar "todos os dias"; adicionar os 7 dias individualmente. Permite analisar desempenho por dia da semana.
- Segmentação por dispositivo (opcional): computador, smartphone, tablet, SO, modelo, tipo de rede (Wi-Fi/4G/5G). Padrão: todos.
- Lances para vendas: Google costuma sugerir "conversões" + "maximizar conversões"; pode manter. CPA-alvo opcional.
- Segmentação para remarketing: "Segmentos de público-alvo" > Procurar > "Como eles interagiram com sua empresa" > visitantes do site, usuários do YouTube, visitantes do app/site.
- Segmentação otimizada: MANTER DESATIVADA em remarketing (se ativada, o Google expande para fora do público selecionado).
- Anúncio: URL final preenche automático; nome da empresa. Imagens: até 15, usar o máximo; ter pelo menos quadrado E horizontal. Logotipo: até 5. Possível adicionar vídeos mesmo em display (aparece em mais formatos: display, Gmail, YouTube). Títulos: até 5. Título longo: até 90 caracteres. Descrições: até 5. Para variações: Duplicar e ajustar poucos elementos.

---

## 7. YouTube (campanhas de vídeo)

### Formatos de anúncio no YouTube
- In-stream pulável (antes de outros vídeos, pulável após 5s): CPV e CPA baratos, tem botão (ideal para CONVERSÃO e inscrição barata via botão). CPE (engajamento) mais caro e CPM mais concorrido.
- Vídeo em feed (antigo discovery: aparece na pesquisa e nos relacionados): exige a pessoa CLICAR para ver (alta intencionalidade), precisa de ótimo título e thumbnail. CPV e CPA mais caros, mas visualização mais qualificada; CPE barato; CPM médio.
- YouTube Shorts: formato vertical (CPV caro, CPA barato); usar sempre que possível.
- Bumper (6s, não pulável): CPM muito barato; dar recados curtos e martelar uma ideia (ex.: "hoje 20h tem aula ao vivo"); aparece muito.
- In-stream não pulável (até 15s): CPM muito barato; também para aparecer e martelar ideia.
- Resumo de uso: conversão/inscrição barata = in-stream pulável; engajamento barato = vídeo em feed; aparecer/lembrar = bumper ou in-stream não pulável.

### Subtipos de campanha de vídeo
- Exibição de vídeos (foco CPV: distribuir conteúdo, fazer ver, aquecer públicos). É o mais usado. Paga só quando alguém decide assistir (True View).
- Alcance eficiente (forçar entrega para muitas pessoas diferentes).
- Frequência desejada (aparecer N vezes para a mesma pessoa).
- In-stream não pulável (inclui bumper e o de 15s).
- Sequência de anúncios (1 anúncio depois outro): "lindo na teoria, fraco na prática"; o autor não usa muito.
- Anúncio de áudio.
- Engajamentos do YouTube (= subtipo para gerar INSCRITOS no canal).
- Impulsionar conversões: NÃO fica mais na campanha de vídeo; para gerar ações/enviar ao site usar o tipo Geração de Demanda (Demand Gen). Muda só a seleção do tipo de campanha.
- Organização: foco em visualização = exibição de vídeo; conversão = impulsionar conversões (em Demand Gen); inscritos = engajamentos do YouTube; alcance = sequência de anúncios + alcance eficiente + frequência desejada + in-stream não pulável + áudio.

### Segmentações no YouTube (super quente > quente > frio)
- Quem quase converteu (acessou LP sem cadastrar / página de vendas sem comprar / add-to-cart sem checkout), sempre excluindo quem converteu.
- Quem viu o anúncio (público de quem viu determinados vídeos: colar as URLs dos anúncios), excluindo quem chegou à página e quem converteu.
- Envolvimento 1 a 30 dias (interagiu com o canal: curtiu/compartilhou/adicionou a playlist/visitou o canal; "comentou" não existe como segmentação).
- Inscritos 540 dias (máximo de período de público no Google Ads; raro estar inscrito em muitos canais = alta intenção).
- Lista de leads (e-mails/telefones).
- Segmentos personalizados (FRIO, funciona muito bem): criar público pelas pesquisas no Google (aparece no YouTube depois, efeito "estou sendo observado"); por sites acessados; por lista de canais/URLs de vídeos consumidos; por apps específicos.
- Público-alvo de mercado (in-market).
- Anúncios de palavras-chave ou canais (segmentação de CONTEÚDO, não de público). Restrição: NÃO se pode segmentar palavras-chave e canais em campanhas de conversão (Demand Gen/impulsionar conversões); usar em exibição de vídeo.
- Estratégia Google Ads de 2 etapas: aparecer na pesquisa E no YouTube via segmento personalizado pelas pesquisas (a maioria dos concorrentes faz só a rede de pesquisa).

### Lance e criação de anúncio no YouTube
- Estratégias de lance para conversão: maximizar conversões (automática) e target CPA / CPA desejado (manual). Recomendação: começar pela MANUAL (target CPA).
- Melhores práticas de criação:
  1. Anúncio deve conversar com a segmentação (gancho direcionado).
  2. Volume muda o jogo (anúncio gravado no celular às vezes bate o cinematográfico).
  3. Pause o que não funciona e ative novos, continuamente.
  4. Hooks são 80/20: se não captar atenção nos 2 a 3 primeiros segundos, perdeu a pessoa.
  5. Anúncios entre 30s e 2 min funcionam melhor (15 min é exceção).
  6. Analisar taxa de visualização (eficiência do gancho) e taxa de conversão: se a de visualização é alta e a de conversão baixa, reaproveitar esse gancho em anúncios que convertem bem.
  7. Testar adiantar o call to action para os ~30s, mas NUNCA esquecer o CTA do final: os melhores anúncios têm 2 CTAs (um ~30s, facultativo, e um no final, obrigatório).

### Criar campanha de YouTube (prática)
- Caminho: Campanhas > Criar campanha (+) > Nova campanha > "Criar uma campanha sem orientação" > Vídeo.
- Subtipo mais usado: "Exibição de vídeo" (True View, paga só quando alguém decide assistir; in-stream, feed ou Shorts).
- Formatos: in-stream pulável (pula após 5s), in-feed (normalmente >=7s), Shorts (mínimo 6s); pode usar os três ou um só.
- Estratégia de lance: CPV. Orçamento diário (ex.: R$40/dia) e datas opcionais.
- Redes: YouTube (padrão); Google TV (só em algumas localizações, ex.: EUA); parceiros de vídeo na rede de display (faz sentido para remarketing; para frio normalmente desativar, mas vale testar). Localização: Brasil. Idioma: todos. Anúncios políticos: ignorar.
- Programação: adicionar 7 horários e trocar "todos os dias" pelos dias individuais (permite análise por dia da semana).
- Grupo de anúncios: nomear. Demográficos: faixa etária e gênero (ex.: 25-54); renda familiar (ex.: faixa de maior renda, removendo "desconhecida"). Interesses: termos como empresários/empreendedores; critérios de porte (empregadores de pequeno/médio/grande porte ajudam a achar quem tem funcionários).
- Expansão de público: DESATIVAR quando se quer anunciar só para o público segmentado.
- Anúncio em vídeo: precisa do link do vídeo já publicado no YouTube. URL de destino opcional. Títulos: título longo e descrição, ambos até 90 caracteres. Nome do anúncio é interno. Dá para duplicar o anúncio e trocar só o vídeo.
- Lance inicial sugerido: começar com mínimo (R$0,05 por visualização, paga por True View de 3s).

---

## 8. Demand Gen e Discovery

- Discovery (Demand Gen): como um Display, mas em público mais qualificado, aparecendo só no feed do Discover, no YouTube e no Gmail (caixa de entrada). Locais qualificados, sem o problema do Display de precisar bloquear sites e receber tráfego ruim.
- Demand Gen hoje abriga as campanhas de conversão de vídeo do YouTube para vendas (o antigo "impulsionar conversões" saiu da campanha de vídeo).

### Setup do Discovery (caso real: padaria em Salvador, encomendas)
- Objetivo Leads; manter só a conversão desejada (ex.: "contatos"). Local específico (Salvador). Idiomas: o professor coloca todos (sugestão alternativa: português + inglês + espanhol).
- Lance: já vai direto para conversão (sem CPC); começar simplesmente com "Conversões" e deixar o CPA desejado para uma otimização posterior. Orçamento ex.: R$30/dia.
- Programação: não dá para otimizar lance por hora, mas deixar os dias certos mapeados (ex.: seg a sáb = 6 dias) e o horário de funcionamento já configurados.
- Aviso: Discovery remove a maioria dos conteúdos sensíveis; exclusões de conteúdo de nível de conta NÃO se aplicam.
- Público: usar o segmento personalizado criado (pessoas que pesquisaram os termos que já convertiam no Search). Opção "usar segmentação otimizada" (Google encontra conversões fora do público): para o primeiro teste, DESMARCAR, para validar se o público é efetivo; depois testar marcado.
- Demográficos: ajustar conforme o cliente (cliente de alta renda: idade a partir de 25, faixas de renda 10% a 30/40% superiores; manter "desconhecido").
- Criativos: 3 posicionamentos de imagem (vertical, quadrado, horizontal); pode adicionar até 20 imagens (usar o máximo); preencher o maior número de títulos e descrições.

### Setup da Performance Max no mesmo contexto
- Objetivo Leads; só a conversão desejada. Lance: conversões ou valor da conversão; começar com Conversões e migrar para CPA depois. Local, idiomas (todos), opção "expansão de URL" (desnecessária se o destino é só uma landing page).
- Grupo de recursos: URL do site; imagens nos 3 formatos; logotipo.
- VÍDEO (sacada para negócio local sem vídeo): se não houver vídeo, usar o botão azul que cria vídeos a partir de um modelo (escolher tempo, fonte, cores, música). O professor criou anúncio em vídeo de 15s no formato Shorts, porque o Google distribui muito Shorts. Sempre criar para não perder o posicionamento de vídeo.
- Títulos: a PMax tem opção de títulos longos; sempre adicionar o máximo de títulos/descrições. Preencher nome da empresa.
- Recursos extras (a PMax permite mais por estar em vários posicionamentos): sitelinks, chamada para ação, promoções, preço, chamada, snippets estruturados, formulário de lead, frases de chamariz, locais.
- Indicador de público (pulo do gato): não é público-alvo "de fato", é INDICADOR. Se o cliente tem lista de compradores, subir essa lista: além de anunciar para ela, o Google cria algo como um lookalike.

### Resultados comparativos (mesma conta, mês de exemplo, custo por conversão em moeda local)
- Search: rodou o mês todo, 196 conversões a CPA 2,58.
- PMax: rodou só o fim do mês (ainda aprendendo), 62 conversões a CPA 2,42.
- Discovery: 188 conversões sem rodar o mês inteiro, cerca de 25.000 impressões, público qualificado (quem pesquisou sobre encomendas), a CPA 1,48.
- Aprendizado: forçar o CPA desejado um pouco abaixo derrubou a Discovery (depois revertido). Forçar demais o CPA pode derrubar a performance.
- Lição: diversificar posicionamentos dá mais força para a conta inteira e melhora o custo médio.
- Bônus ChatGPT (brainstorm, não muleta): pedir copy persuasiva com base no link do site; nova landing page com X seções; títulos/descrições mais criativos para Search; ideias de palavras-chave; over delivery (framework de novo site). O ChatGPT lê o site e pode revelar oportunidades.

---

## 9. Campanhas de visitas à loja

- Dois pré-requisitos: (1) Google Business Profile associado à conta e BEM configurado; (2) saber criar campanha Performance Max. Se o Business Profile não estiver bem configurado, a campanha não funciona bem.
- Estratégia CRÍTICA das metas de conversão (primordial): ao começar, a campanha tem só duas metas disponíveis, "Contato" e "Ver rota". Começar selecionando "Ver rota".
- A cada 2 a 3 dias, voltar à campanha e clicar em Editar. Após um tempo (não determinado: dias, semanas ou 1 a 2 meses), aparece a nova meta "Visitas à loja" (o Google identifica via GPS/Google Maps quem visitou a loja).
- Quando "Visitas à loja" aparecer, editar e trocar a meta para ela. A campanha passa a performar 5 a 10 vezes melhor.
- Erro comum: achar que esse tipo de campanha não funciona porque começa com "Ver rota", não performa bem e a pessoa pausa ANTES de a meta "Visitas à loja" aparecer. É preciso esperar e trocar a meta quando a opção surgir.

### Criar visitas à loja (prática)
- Caminho: Campanhas > ícone de mais. Selecionar "Visitas a lojas locais e promoções" e depois "Performance Max".
- Meta de conversão: manter apenas uma ativa (Contatos ou Ver rota); para esse tipo, normalmente "Contatos".
- Escolher quais lojas o anúncio promove: manter todos os locais ou usar "grupos de locais" para um local específico. Se o local não estiver cadastrado, criar novo (nome e concluir).
- Informar página de destino e nomenclatura. Daqui em diante, igual a uma PMax padrão (lances foco em conversões, CPA-alvo opcional; idioma todos; excluir "telas de TV"; grupo de recursos completo; CTA "Saiba mais"; sitelinks sem repetir a mesma URL; temas de pesquisa; indicadores de público).
- Orçamento: "definir orçamento personalizado". Alerta informativo permite prosseguir; erro em vermelho exige ajuste. Publicar.

---

## 10. Lances e orçamento no Google Ads

- O leilão é afetado por 3 fatores: lances, taxa de ação estimada e qualidade do anúncio.
- Lance pode ou não estar atrelado ao orçamento. Na Meta (99% dos casos) lance está conectado ao orçamento. No Google são INDEPENDENTES: dá para colocar orçamento gigante e a campanha não gastar tudo se o lance for baixo (carro potente travado na primeira marcha). Em geral, gastar mais exige lance maior.
- Google permite lance automático (orçamento e lance andam juntos) ou manual (independentes). No Google o lance manual é mais trabalhoso, mas em muitas situações traz mais resultado.

### Distinguir automáticas x manuais pelo nome (primeiro passo)
- Estratégias AUTOMÁTICAS têm a palavra "máximo"/"maximizar": garantem gastar o investimento, mas NÃO estipulam o valor por resultado.
- Estratégias MANUAIS têm a palavra "desejado": você define o valor; NÃO garantem gastar tudo, mas o Google tenta manter o valor estipulado por resultado (pode até não gastar nada se o lance não for competitivo).

### Siglas
- CPA = custo por ação (conversão); CPC = custo por clique; CPM = custo por 1000 impressões; CPV = custo por visualização.

### As estratégias por grupo
- GRUPO CPA (conversão):
  - CPA desejado (manual): tenta manter o custo por conversão definido.
  - ROAS desejado (manual): tenta manter o ROAS definido.
  - Maximizar conversões (automática): máximo de conversões gastando o investimento, sem estipular valor.
  - Maximizar valor da conversão (automática): foca no valor/dinheiro que entra; gasta o investimento, sem estipular ROAS.
  - CPC otimizado (eCPC), a "pegadinha" (não tem "máximo" nem "desejado", tem "otimizado", que "rima" com desejado): não garante gastar tudo, tenta manter o CPC desejado focando em converter os cliques; classifica-se em CPA por buscar uma ação.
- GRUPO CPC (cliques): CPC manual (define valor por clique, pode não gastar tudo) e Maximizar cliques (gasta tudo, sem definir valor por clique).
- GRUPO CPM (visibilidade/impressões): Parcela de impressões desejada (rede de pesquisa, foco em aparecer no topo mesmo sem clique); CPM desejado (aparecer o máximo, no topo ou não); vCPM / CPM visível (foco 100% em o anúncio aparecer inteiro e ser visto, ex.: banner que não fica cortado ao rolar).
- GRUPO CPV (visualização): CPV desejado (define o valor por visualização) e CPV máximo (não define valor, gasta todo o dinheiro).
- Não há regra universal de qual estratégia é melhor; depende do tipo de campanha. Estratégia de lance é teste (um dos mais importantes), com recomendações por tipo de campanha.

### Lance vs orçamento na otimização
- Na Meta lance está atrelado ao orçamento. No Google são independentes.
- Nas estratégias não automáticas, pode aumentar muito o orçamento sem aumentar o lance e o Google não gastar (precisa de lance competitivo). Se não gastou, aumentar o lance, mas isso pode explodir o custo por resultado.

---

## 11. Métricas e métricas específicas da rede de pesquisa

- Buscar CTR na rede de pesquisa, no Brasil, na maioria dos nichos, acima de cerca de 8 a 10%.
- Objetivo: saber que essas métricas existem e o que cada uma indica (não decorar).

### Métricas específicas de Search
- "Índice de share perdido pela classificação na primeira posição": % de vezes que seus anúncios poderiam ter aparecido na 1ª posição mas não apareceram. Causas: falta de qualidade do anúncio, lance baixo ou (principalmente) falta de orçamento, sinal para aumentar orçamento (sempre cruzar com a métrica principal).
- "Porcentagem de impressões na primeira posição": % de vezes que o anúncio apareceu na 1ª posição. Serve para responder ao cliente clássico ("pesquisei meu nome e não apareceu"): o Google é leilão e nem sempre mostra o anúncio (testa não mostrar / mostrar concorrentes / sem anúncios). Cruzar com "impressões" (quantas vezes apareceu de fato); buscas isoladas do cliente não dizem nada.
- "Índice de share da parte superior da pesquisa": % de impressões recebidas entre os anúncios da parte superior (que recebe mais cliques).
- "Parcela de impressões perdidas na rede de pesquisa (orçamento)": estima a frequência com que o anúncio não apareceu por orçamento baixo. Diz literalmente "você não aparece porque investe pouco".
- "Índice de share de impressões perdidas, primeira posição da pesquisa (orçamento)": frequência com que o anúncio não foi o 1º por orçamento baixo, "aumente o orçamento para aparecer na 1ª posição".
- "Parcela de impressões perdidas na rede de pesquisa (qualificação)": estima quantas vezes o anúncio não foi exibido por classificação insatisfatória (qualidade). Corrigir melhorando copy, títulos e os termos de pesquisa em que aparece.
- Padrão: as métricas de "orçamento" pedem investir mais; as de "classificação/qualificação" pedem melhorar a qualidade do anúncio.
- CTR alto não garante boa classificação: dá para ter CTR alto e ainda perder muitas aparições por qualificação. CTR é forte indicativo, mas a métrica de impressões perdidas por classificação é melhor sinal.

### Editar colunas (prática)
- Caminho: Campanhas > aba "Colunas" > "Modificar colunas". Métricas organizadas por grupos (ex.: "Resultados", "Performance"); para achar uma específica, usar a lupa/busca (ex.: "cliques").
- Reorganizar arrastando; remover com o "X". O Google exibe muitas métricas não usadas (ex.: pontuação de otimização, impressões visíveis, CPM médio visível, CTR visível, tipo de estratégia de lance); manter só as relevantes.
- Conjunto de colunas relevante sugerido: custo, conversões, custo por conversão, cliques, CPC médio, impressões, CTR.
- Salvar: "salvar conjunto de colunas" na parte inferior, dar nome (ex.: "métricas subido"), "salvar e aplicar".

---

## 12. Otimizações específicas do Google Ads

- O Google tem locais de otimização que outras plataformas não têm. As otimizações principais (lance, orçamento, público, criativo, destino, pixel, estrutura) continuam valendo; estas aqui são, em sua maioria, "cereja do bolo" (baixo impacto), EXCETO a de termos de pesquisa. Erro comum: gastar horas nelas e deixar de fazer as que mais importam.
1. Termos de pesquisa (rede de pesquisa): o menu mostra o que a pessoa digitou para o anúncio aparecer. Remover na hora termos absurdos/sem nada a ver. Cadência: a cada 7 dias no início; a cada 15 quando estável; a cada 30 quando madura. Termos que não geram conversão qualificada: revisar 1x/semana, depois 1x/15 dias, depois 1x/30 dias.
2. Onde os anúncios são exibidos (YouTube e Display): ver em quais vídeos/sites apareceu e excluir os sem noção. Mesma cadência dos termos.
3. Programação (dias/horários): no Google define-se em quais dias e horários aparecer (no Meta só com orçamento total/vitalício). Ver o resultado médio por dia da semana e ajustar lance por dia ("aumente meu lance em 1%, 2%, 5% nesse dia"). Hoje o Google é mais estável. Cadência: a cada 2 semanas no início, depois 1x/mês.
4. Locais (segmentação geográfica): ver performance por estado/cidade e aumentar lance em X% para regiões com resultado muito bom. Cadência: a cada 2 a 3 semanas no início, depois 1x a cada 1 a 2 meses.
5. Dispositivos: ajustar lances por celular, computador, TV, tablet. Cadência: 1x/semana inicialmente, depois 15 dias, depois ao menos 1x/mês (1 a 2 min só para bater o olho).
6. PMax: otimizar grupos de recursos e grupos de fichas (principalmente em e-commerce, otimização de grupo de fichas). Cadência: 1x/semana.
- Habilidade-chave: razoabilidade/seletividade para escolher o que fazer. Caso real: tirar horas de otimização de "locais" de 10 a 15 clientes melhorou os resultados ao liberar energia para o que importa.

### Método de otimização por Índice de Qualidade (MOIQ)
- Índice de qualidade = formalização do "bolo de cenoura fofinho". 3 pilares: RELEVÂNCIA DO ANÚNCIO, CTR ESPERADO, EXPERIÊNCIA NA PÁGINA DE DESTINO.
- O Google atribui nota aos 3 pilares, MULTIPLICA pelo lance e gera a nota final que define a POSIÇÃO no ranking. Mito: pagar mais para aparecer primeiro não funciona; dá para aparecer na frente pagando metade ou menos do clique do concorrente.
- RELEVÂNCIA: correspondência entre o que se anuncia e a intenção da busca. Boa relevância aumenta CTR; cumprir a jornada inteira (clicar + agir na página) eleva a nota e o Google bonifica.
- CTR (cliques/impressões): atratividade do anúncio.
- EXPERIÊNCIA NA PÁGINA: se a pessoa pesquisou, clicou, chegou e converteu, a experiência foi positiva.
- Como ver: campanha > grupos de anúncio > palavras-chave > Colunas > Modificar colunas > Todas as colunas > Índice de qualidade. Traz 8 métricas (cada pilar + sua versão "histórico"). Tudo com "HISTÓRICO" usa OUTROS anunciantes como base; sem "histórico" é seu, é nesse (o seu) que se deve focar.
- Código de cores mental: ABAIXO DA MÉDIA = vermelho/crítico; NA MÉDIA = amarelo (melhorar); ACIMA DA MÉDIA = verde (ok). Otimizar tudo que estiver abaixo OU na média.
- DICA DE OURO: quando aparece TRACINHO ("-") num pilar, é porque o Google não teve dados suficientes; nesse caso analise CTR e TAXA DE CONVERSÃO da palavra para decidir (por isso adicionar essas duas colunas).
- Cuidado: não mexer demais no título e derrubar a taxa de conversão; o problema pode ser o TEXTO/relevância, não a página. Exemplo real: termo com índice 3, CTR na média, experiência e relevância abaixo da média, MAS taxa de conversão de 50%, não mexer na página; ajustar o anúncio ou isolar o termo num conjunto/página específicos.
- O que o Google diz para subir cada pilar:
  - RELEVÂNCIA abaixo/na média: linguagem do anúncio igual/semelhante à pesquisa; separar grupos de anúncio e agrupar palavras-chave por tema ("cada palavra na sua prateleira"). ESPECIFICIDADE é tudo.
  - CTR muito abaixo: tornar o texto mais relevante e atraente (títulos e descrições); conferir se o texto corresponde à intenção da palavra; destacar benefício exclusivo (frete grátis, 10% off) unido a CTA. Anúncios muito específicos podem ter CTR menor, aí avaliar pela TAXA DE CONVERSÃO.
  - PÁGINA DE DESTINO: a página deve ter o que o usuário pesquisa; usar a taxa de conversão como indicador (conversão alta = página ok); página responsiva; carregamento rápido.
- BÔNUS SEO ("bolo de cenoura 2.0 com fermento"): o robô do Google indexa a página, lê e, se relevante, rankeia.
  - Colocar a PALAVRA-CHAVE no TÍTULO da página, na SLUG da URL (tudo após o domínio) e no H1.
  - Respeitar a HIERARQUIA de títulos H1-H6 (só um H1 por página); estrutura H1 > parágrafo > H2 > parágrafo > H3 > CTA. ERRO comum: trocar H1/H2 por H3/H4 só para diminuir a fonte (o Google lê isso e destrói o ranking). Pedir ao desenvolvedor para respeitar a hierarquia e usar CSS para o tamanho.
  - Estrutura completa replicada em todas as páginas (palavra no título + slug + H1 + conteúdo) gerou melhora absurda de performance.

---

## 13. Conversões e tag do Google

- A tag do Google Ads é o "pixel do Google" (nomes mudam o tempo todo). O atemporal é entender o que é a tag e como funciona.
- TAG x AÇÃO DE CONVERSÃO:
  - TAG do Google Ads = o pixel, é ÚNICA (uma só por conta) e deve estar em TODAS as páginas do site. É um código.
  - AÇÃO DE CONVERSÃO = equivalente ao evento; uma para cada coisa que quer medir, instalada na página onde a ação é medida. Ex.: para medir cadastro, a tag fica em todas as páginas e, quando a pessoa preenche e vai para a página seguinte, a presença da tag + ação de conversão nessa página indica que a conversão ocorreu.
- 3 funções da tag (iguais às do pixel da Meta): (1) informante (informa o que acontece no site, qual público/anúncio vende); (2) cérebro da conta (treina o algoritmo para direcionar melhor); (3) criar públicos (quem foi ao site, quem realizou ações).
- Instalação: usar Google Tag Manager (há curso específico). Não precisa programar; basta saber ENCONTRAR os números de identificação.
  - Na TAG, identificar o número ao lado das letras "AW" (ex.: AW-11354001425). Esse número é único e SEU; não usar a tag de outra pessoa.
  - Na AÇÃO DE CONVERSÃO, identificar o ID dela.
- 3 formas de instalar a tag/ação de conversão: (1) manualmente; (2) enviar instruções por e-mail a um desenvolvedor; (3) Google Tag Manager (a melhor, recomendada). Na instalação manual, clicar em "ver snippet de evento" para ver o código da ação de conversão; nele há a identificação da tag (ao lado de "AW") e a da ação de conversão (o "monte de letra e número" ao lado).
- Toda ação de conversão criada fica disponível ao criar campanha com objetivo de vendas ou leads.

### Configurações de uma ação de conversão
- Otimização de meta / categoria: o que a conversão representa (compra, lead etc.).
- Nome da ação de conversão.
- Valor: pode ser zero (cadastro gratuito não tem valor); fixo se for sempre o mesmo (ex.: R$100); dinâmico para e-commerce com valores diferentes.
- Contagem: contar UMA vez ou TODAS as vezes por pessoa. Selecionar "UMA" para evitar duplicidade (ex.: pessoa que compra e depois atualiza o cartão não gera 2 conversões; "todas" duplicaria).
- Janela de clique, janela de visualização engajada, janela de visualização e modelo de atribuição.

### Criar ação de conversão (prática)
- Configuração de metas/conversões: Metas > Resumo. A tag de conversão é diferente da tag principal: dispara APENAS quando ocorre a conversão.
- Criar: escolher o tipo (ex.: compra) > criar conversão > selecionar a tag de site criada > "manual com código" > manter como ação primária > nomear.
- Instalação da tag de conversão: snippet de evento, instrução por e-mail ou Google Tag Manager (recomendado GTM).

---

## 14. Problemas comuns no Google Ads

### Problema A: "Minha campanha não gasta dinheiro" (na ordem)
1. Verificar a DATA/período analisado (erro bobo e comum: analisar período do passado quando ativou a campanha ontem).
2. Verificar aprovação dos anúncios (rejeitados por política ou aguardando aprovação).
3. Olhar os lances: lance muito baixo deixa a campanha não competitiva. Aumentar. Técnica de segurança: REDUZIR o orçamento a um valor onde, se o Google gastar 5x, não há problema; e então aumentar muito os lances (chegando a dobrar o lance a cada 1 hora, atualizando e checando). Reduz-se o orçamento para evitar que, com lance muito alto + orçamento alto, o Google gaste a verba do mês inteiro em um dia.
4. Verificar se a segmentação não está restrita demais: remover ressegmentações, remover exclusões e expandir o público. Técnica: criar campanha paralela com público bem mais amplo e seguro (ex.: in-market) e aguardar aprovação.
5. Alterar a estratégia de lance, dando "passos para trás": de CPA para CPC, de CPC para CPM. Quanto mais simples a ação, mais a campanha tende a gastar (CPM gasta mais fácil que CPC, que gasta mais fácil que CPA). Ou sair de manual para automatizada (maximizar conversões/cliques).
6. Orçamento muito baixo (dificilmente a causa, mas possível): aumentar.
7. Problema de pagamento: revisar formas de pagamento (cartão recusado). O Google Ads tem telefone por país (no manual) para ligar e entender por que não gasta.
8. Abrir ticket de suporte com o Google.

### Problema B: "Minha campanha gasta toda a verba em um único grupo de anúncio"
- Diagnósticos:
  1. Um público muito amplo e os outros muito pequenos: a ferramenta joga mais verba no maior. Solução: rebalancear o tamanho dos públicos.
  2. Um público traz muito mais resultado que os outros: pode não haver muito o que fazer; pode isolar os outros 4 em outra campanha (em geral vai descobrir que esses 4 eram ruins mesmo).
  3. Um grupo com lance muito maior que os outros (ex.: 50 vs 5/5/5/5): natural gastar mais nele.
- Soluções:
  1. Regular os lances (sempre a primeira): pisar no freio no que gasta muito, acelerar nos que gastam pouco.
  2. Expandir o público do grupo que não gasta: tirar ressegmentação e exclusão; ampliar a janela (ex.: de "viu vídeo no YouTube nos últimos 7 dias" para "últimos 30 dias").
  3. Isolar em outra campanha os grupos que NÃO estão gastando (forçar gasto). Normalmente não dá bom, mas é por conta e risco.
  4. Isolar em outra campanha o grupo que gasta MAIS, só se ele NÃO estiver gerando resultado; se gasta muito E gera muito resultado, não mexer ("não mexe no time que está ganhando"), nesse caso pausar os outros 4 e subir esses 4 numa nova campanha.

### Nichos sensíveis no Google
- Antes de pegar um cliente, ler as políticas de publicidade de TODAS as plataformas onde vai anunciar. Lógica recorrente: "os bons pagam pelos maus".
- Comparado à Meta, Google e TikTok são mais restritivos e cortam logo na primeira fase (criativo), pois nem sempre conseguem ver o que há após o clique. Nichos sensíveis (estética, saúde) passam mais fácil na Meta que no Google.
- Nicho sensível inesperado 1, reparos/serviços: formatação de computador, troca de peça, serviços para celular, serviços de eletrodoméstico, qualquer reparo. Levam muito bloqueio. Houve casos de quadrilhas que recheavam o local de eletrônicos e desapareciam. Hoje muitas vezes é preciso autorização/ser autorizado da marca.
- Nicho sensível inesperado 2, shows e eventos musicais: dão bloqueio no Google (mesmo rodando bem no Meta). É preciso enviar informações ao Google (qual URL vai anunciar) e passar por validações antifraude (já houve eventos falsos anunciados).
- Lição: não presumir resultado fácil; entender bem o que vai anunciar e ler as políticas (também citados: supermercado, loja de churros).

---

## 15. Google Ads Editor

### Conceito
- Aplicativo oficial do Google (Windows ou Mac) para trabalhar OFFLINE. Baixa todas ou algumas campanhas (precisa de conexão para baixar/publicar) e edita offline.
- Vantagem principal: VELOCIDADE (não é só sobre trabalhar sem internet). Copiar/colar e duplicar campanha em 1 segundo. Quem sabe usar faz qualquer alteração cerca de 5x mais rápido; também há mais opções de criação que no Google Ads online.
- Curva real: a primeira semana é horrível e mais lenta; da 2ª à 5ª semana a velocidade dispara (relato: subir campanhas passou de 4 horas para 20 a 30 minutos). 99% das pessoas não vão aprender por preguiça; só se aprende mexendo.
- O que o Editor faz melhor:
  - Otimizações em massa / Localizar e substituir: trocar uma URL/palavra/data em 50 a 100 anúncios, títulos ou descrições de uma vez.
  - Duplicar campanhas e grupos muito rápido.
  - Converter rede de uma campanha: duplicar uma campanha de YouTube e transformá-la em Display (e vice-versa), incluindo toda a hierarquia de grupos/públicos. No Google Ads online não dá.
- O que o Google Ads online faz melhor: leitura de métricas, otimização de campanhas, pequenas alterações, e subir anúncios na rede de display / gráficos.
- Cuidado: alterações em massa são bônus E ônus ("o problema é a solução e a solução é o problema"), podem gerar erros em massa.
- Ordem: primeiro aprender a subir campanha no Google Ads; só depois arriscar no Editor. O ganho no médio prazo é de DIAS (até semanas) de trabalho poupados.

### Google Ads Editor na prática
- Instalação: pesquisar "Google Ads Editor", acessar a página oficial, download e instalar.
- Sincronizar contas: canto superior esquerdo > Conta > Abrir. Mostra as contas vinculadas ao e-mail logado. Para nova conta: "Adicionar" > login + 2FA. Abrir a conta com duplo clique > "Abrir".
- Layout: esquerda = nível de navegação (campanhas, grupos, anúncios, palavras-chave e segmentação); centro = elementos selecionados (lista); direita = ajustes/segmentação. Campanhas desativadas aparecem em tom diferente, mas editáveis. Manter apenas uma selecionada ao ajustar.
- Filtro importante: verificar se "ocultar tipos vazios" está ativado; se estiver, DESATIVAR para ver todos os grupos e anúncios.
- Configurações de campanha: status, nome, orçamento, estratégia de lances, parceiros de pesquisa, rede de display, datas, idioma, localização, outras segmentações.
- Boa prática: manter o Editor numa tela e o Google Ads online noutra, para recorrer à interface original em caso de dúvida.
- Duplicar elementos: botão direito sobre o grupo > Copiar > clicar fora > Colar. Se o nome duplicar, ajustar a nomenclatura. Novos elementos aparecem em negrito.
- Anúncios: ao ver todos não fica claro a qual grupo pertencem; para filtrar, voltar a Grupos de anúncio, selecionar UM grupo e voltar a Anúncios.
- Alterações em massa em anúncios: selecionar múltiplos; campos iguais recebem a alteração em todos; campos diferentes exibem "varia" e mantêm o texto original.
- Palavras-chave: esquerda > Palavras-chave e segmentação. Duplicar: Copiar > Colar e escolher onde inserir. Keyword duplicada gera erro (editar e ajustar). Inserir termo, escolher tipo de correspondência (ampla, frase, exata), definir status.
- Duplicar anúncios entre campanhas: em Anúncios, selecionar um > Copiar > escolher outra campanha > selecionar os grupos > Colar. Se houver conflito por limite de anúncios ativos, pausar excedentes para resolver o erro.
- Publicar: "Publicar" no canto superior direito; pode publicar só a campanha selecionada ou todas com alterações; revisar e confirmar. Os ajustes são aplicados imediatamente na conta.

---

## 16. Recursos (extensões) no Google Ads (prática)

- Acesso: Campanhas > menu Recursos > Recursos > "Criar recurso". Pode ser feito aqui ou durante a criação da campanha. Muitos recursos têm nível: conta, campanha ou grupo de anúncios.
- Imagem: escolher campanha (ou "concluído" para não vincular agora) > Imagens > selecionar. Recomendação: cerca de 20 variações. Salvar.
- Nome da empresa: nível conta ou campanha; inserir o nome; salvar.
- Logotipo: biblioteca, site/rede social ou upload. Só permite UM recurso. "Limite de entidades excedido" = já existe logotipo (editar o existente).
- Sitelink: nível conta ou campanha. Texto do sitelink (limite 25 caracteres); descrição linha 1 e linha 2 (frase contínua); URL final (pode diferir da principal). Até 6 sitelinks por vez. Salvar.
- Frases de destaque: pequenos textos que reforçam pontos. Boa prática: incluir palavras do segmento (ex.: "subido", "comunidade subido", "Pedro Sobral"); adicionar várias.
- Snippet estruturado: destaca características/categorias. Escolher idioma e tipo de cabeçalho (ex.: "cursos"); adicionar valores que são CATEGORIAS, não preços (ex.: "curso de tráfego pago", "curso de traqueamento"). Limite 25 caracteres por item.
- Ligar (chamada): incentiva chamadas. Escolher país (padrão vem Estados Unidos, alterar para Brasil); número no formato código do país + DDD + número. Já vem com ação de conversão ativa.
- Formulário de lead: captura leads pelo anúncio. Título, nome da empresa, descrição; perguntas (nome, e-mail, telefone), cada campo obrigatório ou opcional; perguntas personalizadas (idioma português); tipos de resposta (curta, múltipla escolha, condicionais); URL da política de privacidade; imagem de fundo opcional; mensagem de confirmação; CTA. Tipo: "otimizar para envios de formulário de lead". Para exportar, conectar CRM/aplicativo ou inserir URL (ex.: WhatsApp no padrão código do país + DDD + número).
- Mensagem: enviar mensagens pelo WhatsApp (preview à direita). Plataformas: Messenger, Zalo, WhatsApp (mais usada). Escolher país; número; mensagem inicial (ex.: "Olá, vim do Google e gostaria de receber mais informações"); CTA; descrição do CTA (ex.: "online agora").
- Local: exibe endereço e horário. Nível conta, campanha ou grupo. Origem: grupos por locais, nenhum, ou todos os locais. "Grupo por locais" indicado para muitas localizações.
- Preço: vários preços de produtos para qualificar. Escolher idioma; tipo de categoria (ex.: serviços); moeda BRL; qualificador (a partir de / até / em média); cabeçalho, preço, descrição; URL específica possível. Recomendação: pelo menos 3 recursos de preço.
- Aplicativo: incentiva download. Plataforma (Android ou iOS), pesquisar e selecionar o app.
- Promoção: destaca ofertas. Ocasião (Páscoa, Natal, Black Friday, Dia das mães); idioma e moeda; tipo (comum: desconto monetário, ex.: R$50, item "tráfego pago"); URL específica; detalhes (ex.: cupom); datas opcionais.

---

## 17. Shopping e e-commerce no Google

- Performance Max para e-commerce sempre funciona muito bem (ver seção 5).
- Google Shopping: para e-commerce no Google Shopping; é classificada como campanha de CRESCIMENTO, não essencial.
- Palavras-chave da marca (Google Ads): essencial para e-commerce, quem pesquisa o nome da marca (ex.: "subido relógios").
- Palavras-chave do nicho/segmento (não da marca), ex.: "comprar relógio": geram menos vendas que a busca pela marca, mas trazem acessos qualificados e se retroalimentam com o remarketing.
- Merchant Center: puxa imagens da loja para anúncios automatizados.
- Em PMax de e-commerce, a otimização de grupo de fichas é especialmente importante (cadência 1x/semana).
- Criar Google Business Profile (Google Meu Negócio) mesmo sem ponto físico ajuda muito o posicionamento no Google.

---

## Formação Bastidores do Digital — inteligência adicional

> Esta seção acrescenta ao KB o que é NOVO ou COMPLEMENTAR ao já documentado acima. Fontes: 5 agentes de destilação da Formação Bastidores do Digital.

---

### Divisão de verba do Google por fase de lançamento

O Google recebe percentuais distintos por etapa — a lógica é complementar ao Meta, não concorrente:

| Etapa | % do orçamento total de cada etapa que vai ao Google |
|---|---|
| Captação | 30% |
| Aquecimento | 30% |
| Lembrete | 50% |
| Evento | 50% |
| Carrinho | 30% |

Lembrete e evento recebem fatia maior no Google porque a Rede de Display tem **CPM muito mais barato** que Meta para remarketing de cadastrados, gerando alta frequência com custo menor.

Em orçamentos pequenos (lançamento ≤ R$5k), Google recebe apenas brand terms (rede de pesquisa) — sem YouTube nem Display.

**Tabela de orçamento Google por porte de lançamento (etapa de captação):**

| Porte do lançamento | Total captação | Google (30%) | Diário Google |
|---|---|---|---|
| R$1M | R$700.000 | R$210.000 | R$7.500 |
| R$500k | R$350.000 | R$105.000 | ~R$3.750 |
| R$100k | R$70.000 | R$21.000 | ~R$750 |
| R$30k | R$21.000 | R$6.300 | R$450 |
| R$5k | R$3.500 | só brand terms | ~R$175 |
| R$2k | R$1.400 | só brand terms | ~R$100 |

---

### Campanhas Google por fase de lançamento

#### Fase: Captação

Fontes recomendadas:

| Campanha | Observação |
|---|---|
| YouTube — TrueView for Action | Principal. Objetivo: Leads; selecionar apenas a meta de Lead; retirar segmentação otimizada em públicos personalizados. |
| Rede de Pesquisa — brand terms | Obrigatório mesmo em lançamentos pequenos; captura quem já pesquisa pelo nome da marca/evento/produto. |
| Rede de Pesquisa — termos do nicho | Ao menos 6 grupos de anúncio por tema; anúncio "bolo de cenoura" — cada anúncio conversa com a palavra do grupo. |

**Hierarquia de campanhas YouTube — público quente (captação):**

1. Viu página de captura + vídeo convite
2. Envolvimento completo YouTube 1d + visitantes do site 1d
3. Visitou blog do lançamento 540d
4. Viu CPLs do YouTube (segmento exclusivo do Google — não disponível no Meta)
5. Viu página de vendas + inscritos nas lives
6. Envolvimento 14d
7. Inscritos nos 2 últimos lançamentos

**Campanhas YouTube — público frio (captação):**

- Frios validados: top 50 palavras-chave da rede de pesquisa, top 10 apps que mais convertem, top 10 canais que mais convertem (dados do histórico), segmentos in-market, afinidade, eventos importantes.
- CBO/segmentação ampla com Segmentação Otimizada ativada intencionalmente: usar com cautela e traqueamento rigoroso.

**Configurações obrigatórias de campanha YouTube:**

- Objetivo: Leads — selecionar **apenas a meta de lead** (não deixar todas selecionadas).
- 6–8 anúncios por grupo de anúncio (recomendação da Central de Ajuda do Google).
- Retirar **segmentação otimizada** ao adicionar público personalizado.
- Desativar **parceiros de vídeo** — rodar apenas no YouTube.
- URL obrigatória: Google exige URL mesmo sem ser o foco; usar link do canal ou página de cronograma.
- Estratégia de lance: **CPA Desejado** — definir o target = custo por lead meta do planejamento.

---

#### Fase: Aquecimento (Google)

- Tipo: Vídeo — **Instream pulável** (YouTube).
- Estratégia de lance: **CPV** (custo por visualização).
- CPV de referência inicial: R$0,20 (se gastar rápido → baixar; devagar → subir).
- Público: cadastrados (lista de e-mails + público de quem viu a página de obrigado).
- Orçamento: 30% do total de aquecimento.
- Campanha criada como: "sem meta" → Vídeo e Exibições de Vídeo.
- Rede: desativar parceiros de vídeo — apenas YouTube.
- Segmentação otimizada: **desativar** ao usar público personalizado de cadastrados.

---

#### Fase: Lembrete (Google)

Mix de formatos obrigatório:

| Formato | % do budget Google (lembrete) | CPM de referência |
|---|---|---|
| Display | 70% | R$10 CPM |
| Bumper (6s não pulável) | ~10% | R$40 CPM |
| Non-skippable (15–20s) | ~10% | R$40 CPM |
| TrueView for Action | ~10% | CPA meta definido no planejamento |

- Display: **obrigatório**; criado como "sem meta" → Display; evento de meta = apenas página de obrigado.
- YouTube bumper/instream não pulável: complementar; usar o formato disponível se houver apenas um tipo de vídeo.
- Público: cadastrados (lista de e-mail importada).
- Criar **anúncios com contagem regressiva** para aumentar urgência.

---

#### Fase: Evento ao vivo (Google)

Campanhas e lances:

| Campanha | Formatos | Lance |
|---|---|---|
| "Aula hoje" | Display 70% + Bumper + Non-skippable + TrueView | Lance padrão |
| "Ao vivo" (janela de 1h) | **Apenas Bumper + Non-skippable** | R$500 a R$1.000 CPM (extremamente alto — garante entrega na janela de 1h) |
| "Aulas liberadas" | Brand search + Display + Bumper + Non-skippable + TrueView | Lance normal |

- Campanha "ao vivo": ativar com **programação de anúncio por horário** (ad scheduling) — não deixar rodar fora da janela. É o único momento em que se sacrifica eficiência por alcance máximo.
- Campanha "aulas liberadas": criar campanha **nova por CPL** liberado; ao lançar CPL 2, pausar a campanha do CPL 1 (sequencial — nunca paralelo).

---

#### Fase: Evento gravado (CPLs)

- Mesma lógica de "aulas liberadas" do ao vivo, sem as campanhas "aula hoje" e "ao vivo".
- Lançar campanha por CPL, pausar a anterior ao avançar.

---

#### Fase: Carrinho (Google)

Google recebe **30%** do orçamento de carrinho. Mix por prioridade:

| Formato | Prioridade | Observação |
|---|---|---|
| Rede de Pesquisa — brand terms | Máxima | Colocar lance mais alto possível; não deixar concorrente aparecer. Obrigatório em todos os portes. |
| YouTube — TrueView for Action | Alta | Vídeo de resposta direta orientado à conversão |
| Discovery / Geração de Demanda | Média | Feed do YouTube/Gmail/Discover |
| Display | Baixa | Menor prioridade no carrinho |

- **CPA de referência inicial** (sem histórico): ticket do produto ÷ 10 — ex.: produto R$1.500 → CPA inicial R$150.
- Controlar CPA por **grupo de anúncio** (não por campanha) para forçar gasto nos públicos mais quentes.
- Estratégia: **CPA Desejado** para rede de pesquisa e YouTube.
- Evento de conversão: **Compra** (no Google funciona bem otimizar diretamente para compra, diferente do Meta onde se usa Initiate Checkout).
- Picos de orçamento também no primeiro e último dia de desconto (espelhar lógica do Meta).

---

### Modelo perpétuo — estrutura base no Google

- Campanhas sempre ativas: **Display de atração** (público frio) + **TrueView de engajamento** (remarketing).
- Testar variações de criativos continuamente — mínimo 1 teste ativo a cada momento.
- Períodos fixos de análise: 7 dias / 3 dias / ontem.
- **Campanha de branded search**: nunca desligar — captura quem pesquisa ativamente pelo nome da marca; é a venda mais barata de todas.

---

### Setup de conversões Google Ads para infoprodutos

Criar **2 ações de conversão** separadas:

1. **Compra** (ação primária, usada para otimização de lances):
   - Categoria: Compra; Meta: ação primária.
   - Atribuição: **Último clique** (não "baseado em dados" — para infoprodutos o último clique reflete melhor a realidade).
   - Contagem: Todas.
   - Conversões otimizadas: ativar.

2. **Checkout / Initiate Checkout** (ação secundária — não otimiza lances):
   - Após criar: editar e mudar para "ação secundária" (o Google não permite alterar durante a criação).
   - Conversões otimizadas: ativar.

**Configurar na Hotmart:**

- Ferramentas → Pixel de rastreamento → selecionar produto → Google.
- Campo "ID de conversão": `AW-[ID]` da campanha de Compra; "Label de conversão": label da ação de Compra.
- Evento de Compra: **desmarcar** "visitas na página de pagamento" (senão conta checkout como compra).
- Adicionar segundo pixel para Checkout: mesmo ID, label do Checkout; desmarcar "vendas realizadas", manter apenas "visitas na página de pagamento".
- Configuração de valor: usar "valor real da venda" (ajuda o Google a otimizar para tickets maiores).

**Configurações obrigatórias antes do lançamento:**

- Google Ads vinculado ao Google Analytics (GA4)
- Google Ads vinculado ao YouTube
- Google Ads vinculado à plataforma de vendas (ex.: Hotmart)
- Pixel/tag criada e instalada
- Eventos padrão e personalizados criados
- Conversões personalizadas criadas e verificadas

---

### Organização de colunas do gerenciador Google Ads

#### Por fase de lançamento

**Captação e vendas (tag: Conversão):**
Campanha | Orçamento | Status | Tipo de campanha | Tipo de estratégia de lances | Custo | Impressões | CPM médio | Cliques | CTR | Conversões | Custo por conversão | Taxa conv. (cliques) [personalizada]

> Métrica personalizada `Taxa conv. (cliques)` = Conversões ÷ Cliques — cria uniformidade entre campanhas de pesquisa e YouTube (a nativa divide por bases diferentes por tipo, tornando a comparação inválida).

**Aquecimento (tag: YouTube):**
Tipo de campanha | Custo | Impressões | CPM médio | Visualizações | CPV médio | Vídeo assistido até 25% / 50% / 75% / 100%

> O Google já fornece os percentuais de retenção nativamente (diferente do Meta, onde é preciso criar métricas personalizadas de CPV por percentual).

**Lembrete e Evento:**
Igual ao padrão de Conversão + métrica de clique no link para a página do evento.

**Vendas (carrinho):**
Campanha | Custo | Impressões | CPM | Cliques | CTR | Custo/clique | Checkouts | Compras | Custo/compra | Taxa de conversão

---

### Cronograma de otimização Google Ads — lançamento

| Tipo de otimização | Frequência |
|---|---|
| Lances de grupo de anúncios ("cage") | **3× por dia** (café, almoço, janta) |
| Orçamento entre campanhas/fontes | 1× por dia |
| Programação (horários), locais, dispositivos, idade, gênero, renda | 1× por semana |
| Públicos (segmentos de audiência) | A cada 2–3 dias |
| Anúncios | A cada 2–3 dias |
| Páginas (landing pages, A/B) | A cada 5–7 dias |
| Estrutura geral de campanha | Somente se resultados muito ruins |

- "Cage" = otimização de lances 3× por dia no Google Ads — usar alarme/despertador (ex.: 9h, 14h, 20h).
- Criar calendário de otimizações antes do início do lançamento.
- Se Meta estiver com CPL melhor que Google: migrar verba para Meta; se Google estiver melhor: migrar para Google.

---

### Crescimento de canal e entressafra (Google)

**Crescimento de inscritos no YouTube:**

1. Criar campanha de vídeo sem meta → subtipo: Inscrições e engajamento com o YouTube.
2. Grupos de anúncio: um para público quente, um para público frio.
3. Estratégia de lance: CPA desejado ou maximizar conversões.
4. Priorizar vídeos curtos (até 1 min — elegíveis para Shorts).
5. URL de destino: `youtube.com/c/[canal]?sub_confirmation=1` — abre o canal com popup de inscrição automaticamente.

**Campanhas de aquecimento na entressafra:**

- Objetivo: engajamento ou visualização de vídeo.
- Segmentos: cadastrados do lançamento (quente) + segmentos frios.
- Métricas: custo por visualização e % de retenção (25/50/75/100%).
- Orçamento entressafra: **10–20% do investimento total do lançamento seguinte** — ex.: lançamento de R$100k → investir R$10k–R$20k na entressafra.

---

### Google Analytics (GA4) — integração obrigatória

Métricas que **não existem no Google Ads** e devem ser monitoradas no GA4:

- Visualizações da página de destino / taxa de carregamento (connect rate).
- Número de pessoas na página das aulas (durante o evento ao vivo).

O Google Ads reporta métricas de campanha; o GA4 reporta o comportamento pós-clique — as duas visões juntas são necessárias para diagnóstico completo do funil.

---

### Diagnóstico rápido — Google Ads no contexto de lançamento

| Problema | Causa provável | Ação |
|---|---|---|
| CTR baixo na pesquisa | Anúncio não conversa com a palavra-chave; falta de relevância | Revisar bolo de cenoura — anúncio e palavra precisam ter o mesmo tema |
| Campanha não gasta (CPA desejado) | Lance CPA muito baixo para o leilão atual | Aumentar CPA em incrementos até gastar o previsto |
| CPL caro no YouTube | Público muito frio ou criativos fracos | Priorizar hierarquia de quentes; testar novos ganchos |
| Campanha "ao vivo" não entrega na janela de 1h | Lance muito baixo para a janela curta | Subir CPM para R$500–R$1.000; usar apenas Bumper e Non-skippable |
| Taxa de conversão baixa vs. Meta | Base de cálculo diferente (Google usa cliques, não visitas LP) | Criar coluna personalizada `Taxa conv. (cliques)` para comparação válida |
