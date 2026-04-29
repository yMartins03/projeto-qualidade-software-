# Atividade PBL – Aula 5  
## Testes Funcionais vs Estruturais – LocalEats

## Integrantes do Grupo
Lucas Fernandes da Silva
Henrique dos Santos Laroque
Adriel Martins de Anunciação
Derick dos Santos Laroque

## 🎯 1. Funcionalidade escolhida

*Funcionalidade selecionada:*  
Busca de restaurantes

*Descrição da funcionalidade:*  
A funcionalidade de busca de restaurantes permite que o usuário pesquise estabelecimentos dentro do LocalEats a partir de informações como nome do restaurante, tipo de comida, localização e filtros disponíveis no sistema. Essa funcionalidade serve para aproximar o usuário do resultado que ele realmente deseja encontrar, facilitando a navegação e tornando a experiência mais prática.

*O que o usuário espera:*  
O usuário espera que a busca apresente resultados corretos, rápidos e coerentes com aquilo que foi digitado ou selecionado, sem exibir itens não relacionados a busca. Além disso, o usuário espera que os filtros funcionem corretamente .

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

*Quais testes vocês fariam sem conhecer o código?*  
Realizaria diversas pesquisas diferentes para verificar se está buscando corretamente conforme o que foi digitado.

### 🔹 Cenários de teste

*Cenário 1:*  
O usuário digita o nome exato de um restaurante.  
*Resultado esperado:* o sistema deve exibir o restaurante pesquisado.

*Cenário 2:*  
O usuário digita apenas parte do nome do restaurante.  
*Resultado esperado:* o sistema deve exibir restaurantes relacionados com o que foi digitado.

*Cenário 3:*  
O usuário pesquisa por um tipo de culinária, como hambúrguer, pizza ou baurú.  
*Resultado esperado:* o sistema deve mostrar restaurantes que tem esse tipo de comida no cardápio.

*Cenário 4:*  
O usuário aplica filtros junto com a busca, como categoria e localização.  
*Resultado esperado:* o sistema deve exibir somente restaurantes que se enquadram no filtro selecionado.

### 🔹 Possíveis erros identificados

Podem ser identificados erros como resultados incorretos, filtros que não funcionam, ausência de mensagem quando não existem restaurantes compatíveis, retorno de restaurantes irrelevantes, lentidão na resposta da busca e comportamentos inesperados em pesquisas com campo vazio ou dados digitados de forma incomum. Também podem aparecer inconsistências entre pesquisas semelhantes, o que prejudica a confiança do usuário no sistema.

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

*Como essa funcionalidade poderia estar implementada internamente?*  
Internamente, a funcionalidade de busca pode estar implementada por meio de regras de validação de entrada, normalização do texto digitado, aplicação de filtros, comparação com os dados cadastrados e ordenação dos resultados antes da exibição final. 

### 🔹 Lógica hipotética (pseudo-código ou descrição)

Ao receber o termo digitado pelo usuário, o sistema pode primeiro validar se o campo está vazio. Em seguida, pode tratar o texto para padronizar caracteres e evitar diferenças entre letras maiúsculas, minúsculas e acentos. Depois disso, pode aplicar os filtros selecionados, como categoria e localização, consultar os dados cadastrados e organizar os resultados conforme regras internas de relevância. Caso não encontre nenhum restaurante compatível, o sistema pode exibir uma mensagem informando que não houve resultados.

### 🔹 Situações a serem testadas

*Situação 1:*  
Verificar se o sistema trata corretamente campos vazios, espaços em branco e caracteres especiais.

*Situação 2:*  
Verificar se a lógica de combinação entre filtros está correta, especialmente quando há mais de um critério de busca ao mesmo tempo.

*Situação 3:*  
Verificar se todos os caminhos internos do código estão funcionando, como busca com resultado, busca sem resultado, restaurante ativo, restaurante inativo e falha de consulta.

### 🔹 Possíveis erros identificados

Nos testes caixa-branca, podem ser encontrados erros como condições lógicas incorretas, filtros aplicados de maneira errada, caminhos de execução que nunca são alcançados, validações incompletas, tratamento inadequado de exceções e falhas na normalização do texto. Essa abordagem ajuda a encontrar defeitos estruturais que nem sempre aparecem claramente para o usuário, mas que explicam a origem de problemas observados na prática.

## ⚖️ 4. Comparação entre as abordagens

*Qual a principal diferença entre testar sem ver o código e com acesso ao código?*  
A principal diferença é a perspectiva adotada. Nos testes caixa-preta, a análise é feita com foco no comportamento externo da funcionalidade, ou seja, naquilo que o usuário informa e no que o sistema devolve. Já nos testes caixa-branca, a análise considera a estrutura interna do sistema, permitindo examinar a lógica, os fluxos e as decisões implementadas no código.

*Que tipo de problema cada abordagem ajuda a encontrar?*

*Caixa-preta:*  
Ajuda a encontrar falhas relacionadas ao comportamento da funcionalidade, problemas de usabilidade, respostas incorretas, inconsistências nos resultados e desvios em relação ao que o usuário espera ou ao que os requisitos definem.

*Caixa-branca:*  
Ajuda a encontrar falhas internas de implementação, como regras lógicas incorretas, validações mal construídas, caminhos do código não testados, erros de tratamento de dados e problemas que afetam a estabilidade da funcionalidade.

## 💡 5. Reflexão no contexto do LocalEats

*Qual abordagem parece mais importante neste momento do projeto?*  
No contexto atual do LocalEats, a abordagem mais importante é a combinação entre testes caixa-preta e caixa-branca. Isso acontece porque os problemas relatados no sistema envolvem tanto erros visíveis para o usuário quanto possíveis falhas internas na implementação. Como há resultados incorretos nas buscas, comportamentos inesperados e inconsistências entre funcionalidades, é necessário avaliar tanto o efeito percebido pelo usuário quanto a lógica que gera esses comportamentos.

*Apenas uma abordagem seria suficiente? Por quê?*  
Não. Apenas uma abordagem não seria suficiente. Os testes caixa-preta são fundamentais para mostrar que o sistema está falhando na experiência real de uso, mas eles não explicam exatamente onde está a origem do erro. Já os testes caixa-branca ajudam a localizar falhas internas com mais precisão, porém sozinhos podem deixar passar problemas importantes do ponto de vista do usuário. Por isso, as duas abordagens devem ser usadas de forma complementar, especialmente em um sistema que já apresenta problemas variados como o LocalEats.

## 🚀 Conclusão

Com esta atividade, o grupo aprendeu que testes funcionais e testes estruturais possuem objetivos diferentes, mas se completam. Os testes caixa-preta ajudam a verificar se a funcionalidade atende ao que o usuário espera e se o sistema responde corretamente às entradas informadas. Já os testes caixa-branca permitem observar a lógica interna da aplicação e identificar falhas que não seriam facilmente percebidas apenas pela interface.

No caso do LocalEats, ficou claro que pensar os testes sob diferentes perspectivas é essencial para compreender melhor os problemas do sistema. A atividade mostrou que qualidade de software não depende apenas de testar resultados finais, mas também de entender como esses resultados são produzidos internamente. Essa visão mais completa fortalece o raciocínio da equipe e aproxima a análise de uma atuação mais profissional em QA.