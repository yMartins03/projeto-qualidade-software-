# Aula 15 - Modelos de Maturidade

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

# 1. Diagnóstico de Maturidade

O diagnóstico abaixo avalia o processo utilizado pela equipe para organizar, desenvolver, testar e entregar as atividades relacionadas ao sistema LocalEats. A análise considera práticas observadas no repositório, nas atividades anteriores e na forma como os artefatos de qualidade foram produzidos.

| Critério | Sim | Parcial | Não | Evidência / Justificativa |
| --- | --- | --- | --- | --- |
| Os requisitos são documentados? |  | X |  | As atividades registram objetivos, fluxos e cenários, mas nem todos os requisitos estão descritos como histórias de usuário completas. |
| Existe controle de mudanças? |  | X |  | O Git registra alterações por commits, porém ainda não há um fluxo formal com abertura, análise e aprovação de mudanças. |
| Há atividades de teste definidas? | X |  |  | A equipe já trabalhou com testes manuais, automatizados, TDD e BDD em atividades anteriores. |
| Os defeitos são registrados? |  | X |  | Defeitos aparecem nas análises e evidências das atividades, mas ainda não são registrados de forma padronizada em Issues. |
| O processo de desenvolvimento é conhecido por toda a equipe? | X |  |  | As entregas são divididas entre integrantes e seguem um fluxo comum de estudo, implementação, validação e documentação. |
| As tarefas são planejadas e acompanhadas regularmente? |  | X |  | Existe divisão de responsabilidades, mas o acompanhamento ainda não é feito em um quadro visual ou backlog formal. |
| Existe padronização para implementação de funcionalidades? |  | X |  | Há padrões em alguns testes e documentos, mas ainda falta uma checklist única para codificação, testes e entrega. |
| Os testes são executados antes da entrega das funcionalidades? | X |  |  | As atividades de testes incluem execução e registro de resultados antes da entrega no repositório. |
| Há revisão de código ou validação por outro integrante da equipe? |  | X |  | Algumas validações são feitas em grupo, mas ainda não existe obrigatoriedade de revisão por pares. |
| A equipe utiliza ferramentas para gerenciamento das atividades? |  | X |  | O GitHub é usado para versionamento e organização das entregas, mas ainda não há uso estruturado de GitHub Projects ou Issues. |
| Os artefatos do projeto são organizados e versionados? | X |  |  | Os documentos, testes e evidências estão organizados na pasta `docs/` e versionados no repositório. |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? |  | X |  | Alguns testes se relacionam aos fluxos escolhidos, mas ainda não há matriz clara ligando requisito, teste, defeito e entrega. |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? |  | X |  | As reflexões das atividades registram aprendizados, mas a retrospectiva ainda não é uma prática formal e recorrente. |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? |  | X |  | Há contagem de testes executados e aprovados em algumas entregas, mas ainda não existem métricas contínuas como cobertura, defeitos abertos ou tempo de correção. |

## Classificação do Processo

**Nível identificado: Gerenciado**

O processo da equipe já possui organização básica, responsabilidades divididas e artefatos versionados no GitHub. As atividades de teste são planejadas e executadas antes das entregas, o que demonstra preocupação com qualidade. Porém, o processo ainda depende bastante da organização manual da equipe e não possui todos os fluxos formalizados. Também faltam métricas contínuas, rastreabilidade completa, registro padronizado de defeitos e revisão obrigatória. Por isso, o processo está acima de um nível inicial, mas ainda não pode ser considerado totalmente definido ou quantitativamente gerenciado.

---

# 2. Lacunas Identificadas

| Lacuna | Impacto no Processo | Prioridade |
| --- | --- | --- |
| Falta de registro padronizado de defeitos em Issues | Dificulta acompanhar quais problemas foram encontrados, corrigidos ou ainda estão pendentes. | Alta |
| Ausência de métricas contínuas de qualidade | A equipe não consegue acompanhar evolução de qualidade com dados como falhas recorrentes, cobertura ou taxa de aprovação. | Alta |
| Processo de revisão por pares não formalizado | Alterações podem ser entregues sem validação de outro integrante, aumentando o risco de defeitos passarem despercebidos. | Média |
| Rastreabilidade incompleta entre requisitos, testes e entregas | Fica mais difícil comprovar que cada funcionalidade possui testes e evidências associadas. | Média |
| Falta de checklist única de entrega | Cada atividade pode ser validada de forma diferente, gerando inconsistência entre os artefatos produzidos. | Média |

---

# 3. Propostas de Melhoria

| Melhoria | Benefício Esperado | Relação com Maturidade |
| --- | --- | --- |
| Utilizar GitHub Issues para registrar funcionalidades, defeitos e melhorias | Centraliza o histórico do trabalho e facilita o acompanhamento das pendências. | Fortalece o gerenciamento do processo. |
| Criar uma checklist de Definition of Ready e Definition of Done | Garante que as funcionalidades entrem em desenvolvimento com critérios claros e sejam entregues com validação mínima. | Ajuda a padronizar o processo. |
| Adotar revisão por pares antes das entregas principais | Reduz falhas, melhora a comunicação e aumenta a confiança na qualidade dos artefatos. | Aproxima o processo de um nível definido. |
| Criar uma matriz simples de rastreabilidade | Relaciona requisito, teste, defeito e evidência, facilitando auditoria e manutenção. | Melhora controle e previsibilidade. |
| Implantar métricas de qualidade | Permite acompanhar quantidade de testes, aprovação, falhas e defeitos recorrentes. | Base para evoluir para gerenciamento quantitativo. |
| Automatizar a execução de testes com GitHub Actions | Reduz validações manuais e garante que os testes sejam executados a cada alteração importante. | Aumenta controle e repetibilidade. |

---

# Conclusão

A equipe apresenta um processo em evolução, com bons sinais de organização, versionamento e preocupação com testes. O nível de maturidade mais adequado é **Gerenciado**, pois há controle básico das entregas e artefatos, mas ainda faltam padronização, métricas e mecanismos formais de acompanhamento. Para evoluir, a equipe deve transformar práticas que hoje são feitas manualmente em um processo mais claro, rastreável e repetível. Com o uso de Issues, checklists, revisão por pares, métricas e automação, o processo tende a se aproximar de um nível **Definido**, contribuindo diretamente para a qualidade do LocalEats.

