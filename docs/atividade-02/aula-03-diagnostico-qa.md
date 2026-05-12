# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software  
> Aula 3 – Papéis, Responsabilidades e Práticas de QA  
> Equipe: [Nome da equipe]  
> Integrantes: Adriel Martins, Derick Laroque, Lucas Fernandes e Henrique Laroque

---

# 1. Diagnóstico da Situação Atual

## 1.1 Papéis atuais identificados

Liste quais papéis vocês acreditam que existem atualmente na startup.

- Desenvolvedor;
- Gerente de Produto;
---

## 1.2 Quem é responsável pela qualidade hoje?

Descreva como vocês acreditam que a qualidade está sendo tratada atualmente.

> Resposta:
- Provavelmente a aqualidade está sendo tratada com os próprios desenvolvedores, que testam enquanto desenvolvem.
---

## 1.3 Problemas identificados

Liste os principais problemas relacionados à falta de organização da qualidade.

- Clientes relatam erros ao finalizar pedidos;
- Restaurantes recebem pedidos duplicados;
- Funcionalidades chegam à produção com defeitos;
- Falta de definição de responsabilidade por garantia de qualidade do software;

---

## 1.4 Impactos desses problemas

Explique quais são as consequências desses problemas para o sistema e para os usuários.

> Resposta:

- A falta de teste acaba entregando um produto incompleto que não cumpre com as necessidades as quais ele foi feito para cumprir;
---

## 1.5 A qualidade é responsabilidade de quem?

Explique se a qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe.

> Resposta:

- A responsabilidade não deve ser da equipe toda, deve ser bem definida entre alguns integrantes da equipe para que hajam testes o suficiente ao ponto de conseguir minimizar ao máximo os erros/problemas.
---

# 2. Papéis da Equipe Propostos

Definam quais papéis deveriam existir na equipe da Local Eats.

---

## 2.1 Lista de papéis

- Desenvolvedor;
- QA;
- Analista de Sistemas;
- DevOPS;
- Gerente de Produto;

---

## 2.2 Descrição dos papéis

Preencha a tabela abaixo:

| Papel  | Responsabilidades principais | Relação com a qualidade |
|--------|------|------|
| Dev    | Desenvolver o produto conforme o combinado com a equipe, corrigir bugs se houverem | Garantir bom funcionamento do projeto e cumprimento dos requisitos e um código limpo|
| QA     | Planejar, executar os testes e identificar e documentar bugs | Identificar bugs se houverem e garantir que as entregas supram a necessidade do cliente |
| DevOPS | Testes estruturais de infraestrutura, Analisar logs, pipelines e comunação de defeitos sitêmicos | Garantir entrega de qualidade para o cliente evitando erros em produção |
| Analista de Sistemas | Levantar, documentar requisitos como responsabilidade e definir as regras de negócio | Evitar ambiguidade nos requisitos e garantis que o sistema faça exatamente o que foi criado para fazer suprindo as necessidades do clinete |
| Gerente de Produto | Definir prioridades e validar entregas | Garantir que o produto final gere lucro para o usuário |

---

# 3. Práticas de QA Sugeridas

Sugira práticas que a startup pode adotar para melhorar a qualidade.

---

## 3.1 Lista de práticas

- Definir um ou mais integrantes da equipe como QA. Definir pelo menos um integrante da equipe como Analista de Sistemas;
- Testar se o produto, alterações ou implementações estão batendo com os requisitos do cliente e se estão suprindo a necessidade dele;
- Testar diversos fluxos/rotas no sistema e verificar se estão todos funcionais principalmente antes de enviar para a produção;

---

## 3.2 Explicação das práticas

Explique brevemente cada prática sugerida.

### Prática 1:
> Descrição:
- Definir bem os cargos de cada equipe para que cada um saiba exatamente o que tem que fazer, de modo que nenhum integrante faça o mesmo trabalho que o outro e que os integrantes da equipe se organizem bem para realizar;

### Prática 2:
> Descrição:
- Verificar se o que o cliente precisa é de fato o que está sendo feito ou se a equipe esta fugindo da linha de raciocínio principal do produto;

### Prática 3:
> Descrição:
- Teste de fluxos, funcionalidades, etc para que quando subir para a produção ou for apresentar ao cliente não tenham bugs em funcionalidades básicas ou campos faltando por exemplo;

---

# 4. Anúncios de Contratação

A startup decidiu contratar novos profissionais. Crie anúncios de vagas.

> Mínimo: 2 vagas

---

## 4.1 Vaga 1 – [Desenvolvedor Fullstack Júnior]

### Descrição da vaga
> Desenvolvedor Fullstack Júnior com capacidade de resolver problemas e disposição de aprender acerca de novas tecnologias

### Responsabilidades
- Desenvolvimento de novas funcionalidades;
- Corrigir bugs;
- Realizar testes;

### Requisitos obrigatórios
- Desenvolvimento front end: HTML, CSS, React, Typescript;
- Capacidade de raciocínio lógico;
- Desenvolvimento back end: SQL, Git, Typescript, API REST,;

### Requisitos desejáveis
- Boa comunicação;
- Jest, Tailwind, Figma, certificação AWS;
- Inglês;

### Certificações desejáveis
- Certificação CTFL Foundation Level e CPRE-FL

---

## 4.2 Vaga 2 – [Desenvolvedor QA - Tester]

### Descrição da vaga
> Procuramos um profissional capaz de garantir a qualidade no desenvolvimento dos projetos da empresa e na entrega de qualidade dos produtos

### Responsabilidades
- Planejar, executar os testes e identificar 
- Criar cenários de testes;
- Documentação de bugs;

### Requisitos obrigatórios
- Certificação CTFL Foundation Level, CPRE-FL;
- Experiência em projetos com testes avançados de fucionalidades;
- Boa comunicação e capacidade analítica;

### Requisitos desejáveis
- Inglês;
- Noções de automação;
- Conhecimento com Git;

### Certificações desejáveis
- Certificações, CT-AI, CT-AcT, CT-MAT, CT-PT, CT-UT

---

# 5. Conclusão da Equipe

Descreva brevemente:

- O que a equipe aprendeu com a atividade
- Principais dificuldades encontradas
- Principais melhorias propostas para a startup

> Resposta:
- Aprendemos a importância que tem em organizar a equipe seja para projetos pessoais quanto para profissionais, isso só demonstra que a organização de funções é um pilar crucial para construção de um projeto. Definindo bem o que cada um irá fazer, resultará em melhor qualidade em todos os pontos. Além disso, cabe sobressair a importância da realização de testes por parte da equipe tester e do restante da equipe também, a qual deverá garantir a entrega de qualidade ao usuário final.
- Criar anúncios de vagas para outros usuários;
- Organizar a equipe e definir bem as funções, sempre garantindo a alta qualidade nos testes de modo que ao menos funcionalidades básicas estejam sendo cumpridas e minizando os erros no sistema;
---

# 📌 Observações (opcional)

Espaço livre para comentários adicionais da equipe.

> 
