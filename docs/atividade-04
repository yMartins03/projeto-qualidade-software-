# 📄 Estratégia Inicial de Testes

## 1. Funcionalidades principais

1. Cadastro de usuário  
2. Busca e listagem de produtos  
3. Carrinho de compras  
4. Finalização de pedido (checkout)  
5. Integração com pagamento  

---

## 2. Níveis de teste

### Cadastro de usuário

- **Teste unitário:**  
Validação de campos (email, senha, CPF) e regras de negócio.

- **Teste de integração:**  
Integração entre frontend, API e banco de dados.

- **Teste de sistema:**  
Fluxo completo de cadastro até armazenamento no banco.

- **Teste de aceitação:**  
Usuário consegue criar conta e acessar o sistema.

---

### Busca e listagem de produtos

- **Teste unitário:**  
Filtros, ordenação e lógica de busca.

- **Teste de integração:**  
Comunicação entre API e banco de dados.

- **Teste de sistema:**  
Busca realizada e produtos exibidos corretamente.

- **Teste de aceitação:**  
Usuário encontra produtos facilmente.

---

### Carrinho de compras

- **Teste unitário:**  
Cálculo de total, quantidade e manipulação de itens.

- **Teste de integração:**  
Sincronização entre frontend e backend.

- **Teste de sistema:**  
Adicionar, remover e atualizar itens no carrinho.

- **Teste de aceitação:**  
Usuário consegue gerenciar o carrinho corretamente.

---

### Finalização de pedido (checkout)

- **Teste unitário:**  
Cálculo de frete, validação de endereço e total da compra.

- **Teste de integração:**  
Integração entre carrinho, endereço e pagamento.

- **Teste de sistema:**  
Fluxo completo de checkout.

- **Teste de aceitação:**  
Usuário consegue finalizar a compra.

---

### Integração com pagamento

- **Teste unitário:**  
Validação dos dados de pagamento.

- **Teste de integração:**  
Comunicação com o gateway de pagamento.

- **Teste de sistema:**  
Processamento completo do pagamento.

- **Teste de aceitação:**  
Usuário realiza pagamento e recebe confirmação.

---

## 3. Prioridades e riscos

### Funcionalidades mais críticas

- Finalização de pedido (checkout)  
- Integração com pagamento  
- Carrinho de compras  

### Justificativa

Essas funcionalidades impactam diretamente o faturamento.  
Erros podem causar perda de vendas, falhas financeiras e inconsistências no sistema.

### Pontos de maior risco

- Integrações externas (pagamento)  
- Cálculo de valores (frete e total)  
- Persistência de pedidos no banco  

---

## 4. Pirâmide de testes

### Maior concentração: Testes unitários

- Mais rápidos e baratos  
- Cobrem regras de negócio críticas  

### Quantidade média: Testes de integração

- Garantem comunicação entre módulos  

### Menor quantidade: Testes de sistema e aceitação

- Mais lentos e caros  
- Mais frágeis  

### Justificativa

Testes unitários são mais eficientes e baratos.  
Testes de alto nível devem ser usados com menor frequência devido ao custo e complexidade.

---

## 5. Testes em produção

### O sistema deveria usar testes em produção?

Sim, de forma controlada.

### Situações

- Uso de feature flags  
- Monitoramento com logs e métricas  
- Testes A/B  

### Justificativa

Permite validar o sistema em ambiente real.  
Deve ser feito com cuidado para evitar impacto negativo no usuário.
