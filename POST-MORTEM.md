# Post-Mortem — Missão de Release

## Time

- Tech Lead: Victória Silvina Gonçalves
- Dev A: Kassil Kayo Rêgo Alexandre
- Dev B: Antonio Nycollas de Holanda Freitas
- QA/Release: Amanda de Aquino Diógenes

## O que funcionou bem

A divisão das tarefas, os comandos do git no terminal, a criação de novas branchs, resolução dos problemas. O fluxo dos Pull Request, conseguimos fazer bem, apesar do que será relatado na próxima questão. Enfim, no geral, tudo funcionou bem. Trabalhamos bem e fizemos tudo em grupo (apesar de cada um ter sua parte específica), o que facilitou bastante pois foi possível ajudar uns aos outros.

## O que deu errado ou foi difícil

- A priori, foi difícil fazermos o rebase; passamos um tempinho nisso. Não estava dando conflito e não sabíamos o porquê. Depois percebemos que o conflito realmente não existia, pois cada um estava atualizando sua própria branch e a develop não estava sendo modificada. Então, o primeiro dev enviou suas alterações para a develop, via PR. Depois, o segundo dev atualizou a develop local e rodou o rebase na sua dev; aí sim deu o conflito. Ele resolveu, abriu PR, corrigiu o que precisou e foi aprovado.
- Percebemos que os primeiros PRs (os dos DEVs), a gente devolveu resposta via comentários, e não via "Request for Changes" para corrigir algo.
Nos demais foi que corrigimos esse erro e usamos essa opção correta para devolver caso necessário.

## Onde usamos rebase (e por quê)

- O rebase foi usado nas branches individuais dos desenvolvedores para sincronizar suas alterações com a branch develop antes de cada um abrir o Pull Request. Foi usado para que a branch de cada um pudesse estar atualizada com a develop, tivesse um histórico mais limpo, e se tivesse algum conflito, fosse resolvido antes de abrir o PR. No nosso caso, o conflito aconteceu com o dev-b, pois o dev-a já tinha enviado suas alterações para a develop primeiro. Então o dev-b executou o rebase depois, e então seus commits foram reaplicados em cima da develop, que já incluía as alterações do dev-a. Apareceu um conflito e ele pode resolver antes de abrir o PR.

## Onde usamos merge (e por quê)

- O merge foi usado para integrar as alterações das diferentes branches por meio de Pull Requests. Por exemplo: usamos merge para enviar alterações das branchs dos devs para a develop; da release para a main; da branch que introduziu o bug para a main; da hotfix para a main; e tambem da hotfix para a develop. Enfim, usamos merge para unir as alterações feitas nas diferentes branches, permitindo que elas fossem incorporadas de forma organizada e segura.

## O que faríamos diferente

- Realizaríamos um planejamento prévio mais detalhado. O guia da atividade foi útil, mas ele não apresentava um passo a passo exato. Então, nos próximos, definiremos com mais precisão as etapas e estratégias antes de iniciar a execução das tarefas. 