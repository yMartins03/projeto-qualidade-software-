# Aula 16 - Qualidade em Metodologias Ágeis

# Entrega PBL - LocalEats

**Disciplina**: Qualidade de Software  
**Instituição**: Centro Universitário Senac-RS  
**Sistema**: [LocalEats](https://local-eats-unisenac.vercel.app/)  
**Repositório**: [projeto-qualidade-software-](https://github.com/yMartins03/projeto-qualidade-software-)

---

## Integrantes

- Lucas Fernandes
- Henrique Laroque
- Adriel Martins
- Derick Laroque

---

# 1. Análise de Práticas Ágeis no Processo

A análise abaixo considera o processo utilizado pela equipe no projeto LocalEats, observando como as práticas ágeis aparecem nas atividades de planejamento, implementação, testes, documentação e entrega.

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| --- | --- | --- | --- |
| Planejamento iterativo | Parcial | A equipe organiza as entregas por atividades PBL e evolui o projeto em partes. | Sim. O planejamento pode ser estruturado em ciclos curtos, com objetivos claros para cada entrega. |
| Priorização de funcionalidades | Parcial | Os fluxos são escolhidos conforme a proposta da atividade e a divisão entre integrantes. | Sim. Um backlog priorizado ajudaria a definir o que tem maior valor ou maior risco. |
| Entregas incrementais | Sim | As atividades são entregues em etapas, adicionando novos artefatos ao repositório ao longo da disciplina. | Sim. Cada incremento pode ter critérios mínimos de validação antes do commit final. |
| Feedback frequente | Parcial | O feedback aparece em testes, reflexões e ajustes feitos durante as atividades. | Sim. Revisões rápidas entre integrantes e retrospectivas deixariam o feedback mais constante. |
| Trabalho colaborativo | Sim | As entregas são divididas entre os integrantes e consolidadas no repositório do grupo. | Sim. A colaboração pode melhorar com revisão por pares e pareamento em partes críticas. |
| Controle visual das atividades | Parcial | O repositório organiza arquivos e histórico, mas não há quadro Kanban formal. | Sim. GitHub Projects ou um quadro Kanban ajudariam a visualizar tarefas pendentes, em andamento e concluídas. |
| Melhoria contínua | Parcial | As atividades possuem reflexões sobre dificuldades e melhorias. | Sim. A equipe pode registrar ações de melhoria e verificar se foram aplicadas nas próximas entregas. |

## Conclusão da Análise

O processo da equipe possui características ágeis, principalmente pela entrega incremental, colaboração entre integrantes e adaptação conforme as atividades evoluem. Porém, algumas práticas ainda acontecem de forma informal. A ausência de um backlog visual, critérios padronizados de pronto e revisão por pares limita a previsibilidade do processo. A equipe pode melhorar adotando práticas simples de Scrum, Kanban, XP e Lean, sem tornar o processo pesado. O principal desafio é transformar a organização que já existe em um fluxo mais claro, visível e repetível, mantendo a qualidade como parte da entrega.

---

# 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| --- | --- | --- |
| Utilizar um quadro Kanban no GitHub Projects com colunas `Backlog`, `Em andamento`, `Em teste`, `Correção` e `Concluído`. | Kanban | Aumenta a visibilidade do trabalho e reduz dúvidas sobre o status de cada tarefa. |
| Realizar uma breve reunião de planejamento antes de cada entrega. | Scrum | Ajuda a alinhar objetivo, responsáveis, prioridade e escopo da atividade. |
| Aplicar revisão por pares antes de considerar uma entrega concluída. | XP | Reduz defeitos, melhora a legibilidade dos artefatos e compartilha conhecimento entre integrantes. |
| Definir limite de tarefas em andamento por integrante. | Lean / Kanban | Evita acúmulo de tarefas abertas e reduz retrabalho causado por troca constante de contexto. |
| Criar retrospectivas rápidas ao final de cada PBL. | Scrum / Melhoria contínua | Permite identificar o que funcionou, o que falhou e quais ações serão aplicadas na próxima entrega. |
| Manter testes automatizados para os fluxos mais importantes do LocalEats. | XP / Qualidade Ágil | Aumenta a confiança nas mudanças e reduz risco de regressão. |

---

# 3. Definition of Ready (DoR)

Uma funcionalidade ou atividade só deve entrar em desenvolvimento quando atender aos critérios abaixo:

| Critério | Descrição |
| --- | --- |
| Objetivo definido | A equipe entende qual problema a funcionalidade ou atividade precisa resolver. |
| Critérios de aceitação descritos | Existe clareza sobre o comportamento esperado e como validar a entrega. |
| Escopo delimitado | O que será feito e o que não será feito está combinado entre os integrantes. |
| Responsável definido | Cada parte da atividade possui pelo menos um integrante responsável. |
| Dependências identificadas | Links, telas, dados de teste, bibliotecas ou documentos necessários foram levantados antes do início. |
| Estratégia de teste planejada | A equipe sabe se a validação será manual, automatizada, BDD, unitária ou por revisão documental. |
| Prioridade definida | A equipe sabe se a tarefa é essencial para a entrega ou se pode ficar para uma melhoria futura. |

---

# 4. Definition of Done (DoD)

Uma funcionalidade ou atividade só deve ser considerada concluída quando atender aos critérios abaixo:

| Critério | Descrição |
| --- | --- |
| Critérios de aceitação atendidos | O resultado final corresponde ao comportamento ou objetivo definido no início. |
| Testes executados | Os testes planejados foram executados e os resultados foram registrados. |
| Evidências registradas | Prints, logs, tabelas ou descrições de resultado foram adicionados quando necessário. |
| Revisão realizada | Pelo menos outro integrante validou o conteúdo, código ou documentação antes da entrega final. |
| Artefatos versionados | Arquivos da atividade, testes e documentação foram organizados no repositório. |
| Defeitos críticos resolvidos | Nenhum erro crítico conhecido permanece aberto para a funcionalidade entregue. |
| Documentação atualizada | O Markdown da atividade descreve claramente o que foi feito, analisado e concluído. |

---

# Conclusão

A adoção de práticas ágeis pode tornar o processo da equipe mais transparente e confiável. O LocalEats já vem sendo trabalhado de forma incremental, com divisão de tarefas e foco em qualidade, mas ainda há espaço para melhorar planejamento, feedback, revisão e acompanhamento visual. A Definition of Ready ajuda a evitar que tarefas com requisitos indefinidos entrem em desenvolvimento. A Definition of Done garante que a entrega não seja considerada pronta apenas por estar implementada, mas também por estar testada, revisada, documentada e versionada. Dessa forma, a equipe consegue ser mais ágil sem abrir mão da qualidade.

