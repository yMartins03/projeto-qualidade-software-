# PBL – Aula 6  
## Planejamento e Execução de Testes – LocalEats

## 1. Plano de Testes

### Objetivo
Validar o funcionamento das principais funcionalidades do sistema LocalEats, garantindo que os fluxos principais operem corretamente e identificando possíveis falhas, comportamentos inesperados e inconsistências.


### Escopo

#### O que será testado:
- Login de usuários
- Busca de restaurantes
- Visualização de restaurantes
- Adição de itens ao carrinho
- Finalização de pedidos

#### O que NÃO será testado:
- Testes de performance
- Testes de segurança
- Testes automatizados
- Compatibilidade entre navegadores

### Funcionalidades selecionadas
- Login
- Busca
- Carrinho
- Pedido

### Estratégia de Testes
- Testes funcionais
- Testes manuais
- Abordagem de caixa-preta (validação do comportamento do sistema)
- Testes baseados em cenários reais de uso (happy path e cenários de erro)

### Responsáveis
- Henrique Laroque, Derick Laroque, Adriel Martins, Lucas Fernandes


## 2. Casos de Teste

### CT01 – Login com sucesso
Dado que estou na página de login  
E que informo um email válido  
E que informo uma senha correta  
Quando eu clico em "Entrar"  
Então o sistema deve redirecionar para a página inicial  

### CT02 – Login com senha inválida
Dado que estou na página de login  
E que informo um email válido  
E que informo uma senha incorreta  
Quando eu clico em "Entrar"  
Então o sistema deve exibir uma mensagem de erro  

### CT03 – Buscar restaurante
Dado que estou na página inicial  
Quando eu busco por "pizza"  
Então o sistema deve exibir uma lista de restaurantes relacionados  

### CT04 – Realizar pedido com sucesso
Dado que estou na página de um restaurante  
E adiciono um item ao carrinho  
Quando eu finalizo o pedido  
Então o sistema deve confirmar o pedido com sucesso  

### CT05 – Finalizar pedido com carrinho vazio
Dado que estou com o carrinho vazio  
Quando eu tento finalizar o pedido  
Então o sistema deve impedir a ação e exibir uma mensagem de erro  

## 3. Execução dos Testes

| ID   | Resultado | Evidência |
|------|----------|----------|
| CT01 | Passou | Login redirecionou corretamente para a página inicial |
| CT02 | Falhou | Sistema não exibiu mensagem clara de erro |
| CT03 | Passou | Busca retornou restaurantes corretamente |
| CT04 | Falhou | Pedido não foi finalizado corretamente |
| CT05 | Passou | Sistema impediu finalizar pedido com carrinho vazio |

---

## 4. Análise dos Resultados

- Total de testes executados: 5  
- Testes que passaram: 3  
- Testes que falharam: 2  

### Principais problemas encontrados:
- Ausência de feedback adequado no login com erro
- Falha no fluxo de finalização de pedido
- Possível inconsistência na validação de ações críticas do sistema

## 5. Reflexão no contexto do LocalEats

### O plano de testes ajudou a organizar melhor os testes?
Sim. O planejamento permitiu estruturar melhor os cenários, garantindo cobertura das principais funcionalidades e evitando testes aleatórios.


### Algum problema só foi percebido durante a execução?
Sim. A falha na finalização do pedido e a ausência de mensagens claras de erro só foram percebidas durante a execução prática dos testes.


### O que melhorariam no processo de testes?
- Criar mais casos de teste cobrindo cenários extremos
- Incluir testes automatizados para regressão
- Melhorar a documentação de erros
- Aplicar testes de usabilidade para melhorar a experiência do usuário


## Conclusão

A aplicação dos testes permitiu identificar falhas importantes no sistema, principalmente relacionadas à validação de ações e feedback ao usuário. O processo estruturado de QA contribuiu para uma análise mais clara e profissional, demonstrando a importância do planejamento e execução organizada de testes em sistemas reais.