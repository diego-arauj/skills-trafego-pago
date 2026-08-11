# Método operacional: como esta skill opera Meta Ads

Este é o "como pensar" da skill. Os scripts executam; este arquivo decide o que executar e
quando. O Claude deve ler antes de qualquer recomendação de estratégia, estrutura, orçamento
ou otimização.

A base é a prática de um gestor que roda contas de nichos variados (serviço local, e-commerce,
profissional liberal, infoproduto), com a rotina de otimização apoiada no método ensinado pelo
Pedro Sobral no Subido de Tráfego. O que está aqui é a síntese operacional de quem executa, não
o material do curso: para o método completo, faça o curso na fonte.

---

## 1. A regra que vale mais que todas as outras

**Criativo é o fator mais importante.** Público bom não salva anúncio ruim. Antes de mexer em
segmentação, estrutura ou lance, pergunte se o anúncio conversa com quem está vendo. O nome da
plataforma é gerenciador de anúncios, não gerenciador de públicos.

Corolário prático: quando o resultado cai, a primeira hipótese é criativo, não segmentação.

---

## 2. Rotina: análise diária, otimização programada

Separe as duas coisas. Elas têm frequências diferentes e confundi-las é o erro mais caro.

- **Análise** é diária. Dez a vinte minutos por conta, batendo o olho no custo por resultado.
  Não gera alteração nenhuma na maioria dos dias.
- **Otimização** é a alteração em si, e vai na agenda. Segunda, quarta e sexta, por exemplo.

Analisar e concluir que não se deve mexer **é** uma otimização. Não analisar e não mexer por
desorganização não é.

**Três coisas disparam otimização fora da agenda:**

1. Resultado despencando. Intervir na hora.
2. Resultado bom demais. Desconfie antes de comemorar: costuma ser erro de medição (pixel ou
   CAPI disparando conversão no clique, evento duplicado). Confira a medição antes de escalar
   em cima de um número falso.
3. Pressão do cliente. Explique que existe método e programação, recomende esperar. Se ele
   insistir, execute, mas deixe registrado que não era a recomendação.

**Frequência por verba diária POR CONJUNTO** (não é verba total da conta):

| Situação | Frequência de otimização |
|---|---|
| Resultado abaixo do esperado, verba alta | 1 a 2 por dia |
| Resultado abaixo do esperado, verba baixa | 2 a 3 por semana |
| Resultado dentro do esperado, verba alta | 2 por semana |
| Resultado dentro do esperado, verba baixa | 1 por semana |

Quanto menor a verba, menos dados, menos otimização. Quanto melhor o resultado, menos
otimização. Sempre analisar os últimos 7 dias.

---

## 3. Os seis parafusos (o que dá para apertar)

Em ordem de frequência de uso:

### 3.1 Orçamento e lance (o mais frequente)

Na estratégia automática ("maior volume/valor"), **orçamento e lance andam juntos**: aumentar
orçamento aumenta o lance. Daí o truque mais útil da plataforma: para baixar o custo por
resultado numa campanha automática, **diminua o orçamento**.

- Diminuir quando: gastou a verba cedo demais, custo acima do esperado, ou para tirar gasto de
  um grupo específico.
- Aumentar quando: não está gastando o que deveria, ou o custo está abaixo do esperado (custo
  barato não é o objetivo; volume dentro do custo-alvo é).

**Rebalanceamento entre campanhas** (a alavanca mais usada no dia a dia): quando uma campanha
tem CPA baixo e outra alto, mova verba da cara para a eficiente até os custos se aproximarem.
Mova em incrementos, espere de 3 a 5 dias, repita quando a diferença voltar a passar de ~30%.
O objetivo não é zerar a diferença, é maximizar volume ao menor custo médio.

### 3.2 Segmentação (a cada 4 a 7 dias)

Cinco movimentos possíveis:

- **Substituição** — pausar o que não funciona e subir público novo. É o coringa, cobre 80% dos
  casos.
- **Expansão e compressão** — expandir quando o CPM está caro (público pequeno demais está
  encarecendo o leilão); comprimir/qualificar quando o CPM está barato mas a conversão está
  baixa.
- **Separação e fusão** — isolar um público que tende a ir melhor sozinho; fundir públicos
  muito parecidos quando os dois estão diluídos e caros.
- **Otimização subjetiva** — olhar a qualidade do lead, não só o custo. Vale para lead,
  engajamento e seguidor; **não vale para venda** (em venda só importa custo, volume e ROAS).
  É legítimo pagar mais caro num público mais qualificado.
- **Otimizar o anúncio em vez do público** — muitas vezes a segmentação está boa e o criativo
  é que não fala com ela.

**Públicos quentes com exclusão em cascata.** Ao montar remarketing, ordene do mais quente ao
mais frio e faça cada nível excluir todos os mais quentes. Sem isso, o público de 60 dias contém
o de 30, o mesmo usuário entra em dois conjuntos e você paga duas vezes pelo mesmo alcance.

```
01_ENG-30D   → inclui ENG-30D  | exclui COMPRADORES
02_ENG-60D   → inclui ENG-60D  | exclui ENG-30D + COMPRADORES
03_ENG-90D   → inclui ENG-90D  | exclui ENG-60D + COMPRADORES
04_SEGUIDORES→ inclui seguidores | exclui ENG-90D + COMPRADORES
```

Em campanha de aquisição, sempre excluir compradores.

Regra de conferência: **o público tem que bater com o nome do conjunto**. Se o conjunto se chama
ENG-30D, o público é o de 30 dias, mesmo que a campanha que serviu de molde estivesse com outro.

### 3.3 Criativos (o parafuso mais importante)

- **Mantenha variedade ativa: 8 a 12 criativos por conjunto**, salvo falta de acervo. A Meta
  usa os criativos em combinação, cada um cumprindo um papel no caminho até a conversão, e
  atribui o resultado ao último. Deixar 1 ou 2 ativos estrangula a otimização.
- Ao pausar um perdedor, suba outro no lugar para manter o volume.
- **Não pause por impaciência.** Critério: gasto acima do custo-alvo estimado e zero resultado,
  ou frequência alta sem conversão. Criativo com gasto muito baixo ainda não rodou o suficiente
  para julgar.
- Teste sempre. Compare de 6 a 8 anúncios ativos, pause o pior, suba um novo. O módulo inteiro
  de otimização se resume a isso.

**Specs (guia oficial da Meta):**

| Item | Valor |
|---|---|
| Feed | 4:5, 1440x1800 (mínimo 600x750) |
| Stories e Reels | 9:16, 1080x1920 |
| Texto principal | 50 a 150 caracteres (o resto vira "ver mais") |
| Título | ~27 caracteres |
| Imagem | JPG ou PNG, até 30 MB |
| Vídeo | MP4, MOV ou GIF, até 4 GB |

**Zona segura em 9:16:** deixe texto e logo fora dos ~14% do topo e dos ~20% da base, onde o
sistema desenha o perfil e o botão.

Em campanhas de reconhecimento e alcance, o rodapé do anúncio (título, descrição e botão) **não
aparece** no feed mobile. A arte precisa se sustentar sozinha.

**Hook rate** (quantos passam dos 3 primeiros segundos) é a métrica de criativo em vídeo que
mais importa. Sem segurar o início não existe clique nem venda depois.

### 3.4 Estrutura (raro, e delicado)

Tipos, na ordem sugerida de teste: por nível de aquecimento (frio, quente, super quente), por
posicionamento, por região, por tamanho de público, por grau de automação, separando campanhas
de teste das de escala, e criando estrutura própria para um público que converte muito.

Quanto maior a verba, mais estruturas. Verba pequena pede simplicidade: 2 ou 3 campanhas por
nível de aquecimento resolvem.

Só mexa em estrutura quando o resultado estiver consistentemente abaixo do esperado, ou quando
um benchmark mostrar alguém do mesmo nicho indo muito melhor com outra estrutura. Teste de
estrutura demora e não sai limpo; não é semanal.

**Testes em CBO com piso de gasto por conjunto:** quando o teste for em CBO, use piso mínimo por
conjunto para garantir que todos rodem, mas preserve verba livre para a Meta deslocar ao
vencedor. Com 2 conjuntos, ~40% de piso cada; com 3, ~20 a 25% cada. Nunca comprometa 100% do
orçamento em pisos.

### 3.5 Pixel

Otimizar todos os dias significa anunciar de forma constante: pixel aquecido é pixel com
histórico do evento que importa. Se ninguém comprou ainda, a Meta não sabe quem é comprador, e
nenhuma segmentação resolve isso.

### 3.6 Destino (o que separa o operacional do estratégico)

Metade do resultado está fora do gerenciador.

1. Desenhe o funil inteiro: impressão → clique → chegada na página → cadastro → atendimento →
   venda.
2. Ache onde se perde gente.
3. Faça tudo que dá para fazer dentro do gerenciador.
4. Compare quantos você mandou ao destino com quantos chegaram ao fim.

O destino é sempre uma landing page ou um atendimento (humano ou IA). Para atendimento, o
diagnóstico mais rápido é se passar por cliente e ver como respondem, ou ler as conversas
antigas. Análise de destino: semanal.

---

## 4. Fase de aprendizado

Acontece **por conjunto**, não por campanha. "Aprendizado limitado" significa menos de ~50
eventos em 7 dias.

Como sair: aumentar orçamento do conjunto, fundir grupos parecidos e diluídos, corrigir o que
está causando pouco resultado (criativo, destino), ou simplesmente não fazer nada. Se está
convertendo a um custo bom, ignore o status. Quem dita sucesso é a métrica principal.

Alteração brusca devolve o conjunto ao aprendizado. Trocar o criativo de um anúncio conta como
edição significativa. Em conjunto que carrega a receita da conta, case a correção com a próxima
troca de criativos, quando ele vai reaprender de qualquer jeito.

---

## 5. Métricas

Uma **métrica principal** por campanha: a última do funil, ligada ao objetivo real. Todas as
outras são secundárias e existem para explicar por que a principal está boa ou ruim.

Sucesso nunca se declara por métrica secundária. CTR ótimo com CPA ruim é CPA ruim.

Ordem do funil: impressões e CPM → alcance → cliques, CTR e CPC **no link** (nunca "todos", que
conta clique em foto de perfil) → sessão e connect rate → lead ou conversa → venda, ROAS e
ticket médio.

Cada etapa tem uma taxa: o percentual que passou da anterior. É lendo as taxas que se acha o
gargalo.

**Nunca atribuir resultado sem quebrar por campanha.** Olhar o número no nível da conta e dizer
"isso veio da campanha X" é chute. Puxe insights por campanha antes de afirmar.

**Detalhamentos que mais rendem:** por idade, por região (costuma revelar concentração forte),
por posicionamento e por plataforma. Selecione uma campanha por vez antes de detalhar, senão a
leitura vira ruído.

---

## 6. Escala

Seis alavancas, da mais óbvia à mais poderosa:

1. Aumentar orçamento (dobrar verba raramente dobra venda; exija incremento real).
2. Alcançar públicos ainda não atingidos.
3. Criar anúncios novos.
4. Cultivar audiência quente com conteúdo, e transformá-la em público.
5. Abrir outra fonte de tráfego.
6. **Melhorar a conversão fora do gerenciador**: landing page, copy, atendimento, follow-up,
   velocidade de resposta. É onde está a maior alavancagem.

A meta é transformar funil em cilindro: achar o vazamento e atacar sempre o mesmo ponto até
parar de vazar.

---

## 7. Regras automatizadas

Servem para não perder dinheiro enquanto você não está olhando. Criar em Regras automatizadas →
Personalizado.

- Para verba maior, prefira **notificar** a desativar: você decide com contexto.
- **Regra de desativar conjunto por ROAS não funciona sob CBO** (só em ABO). Em conta CBO, use
  notificação.
- Para negócio que só vende em certos dias, duas regras (uma que desativa, outra que ativa)
  resolvem a operação sem depender de ninguém lembrar.

---

## 8. Documentar é parte do trabalho

A maior causa de perda de cliente não é resultado ruim, é falta de clareza sobre o que está
sendo feito. Registre as otimizações: o que mudou, por quê, o que se esperava e o que aconteceu.
Serve como prova do trabalho e como inteligência acumulada da conta.

Esta skill grava isso automaticamente quando você configura o registro de histórico (ver
`SKILL.md`, seção "Registro de histórico").
