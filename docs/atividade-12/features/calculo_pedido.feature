# language: pt
Funcionalidade: Cálculo de pedido no LocalEats

  Como usuário do LocalEats
  Quero calcular o total do meu carrinho
  Para saber o valor antes de finalizar o pedido

  Cenário: Carrinho vazio tem total zero
    Dado que o usuário tem um carrinho vazio
    Então o total do carrinho deve ser 0.0

  Cenário: Adicionar item atualiza o total
    Dado que o usuário tem um carrinho vazio
    Quando adicionar "Pizza Margherita" por 45.90
    Então o total do carrinho deve ser 45.9

  Cenário: Aplicar desconto de 10 por cento
    Dado que o usuário tem um carrinho vazio
    Quando adicionar "Hambúrguer Artesanal" por 35.00
    E aplicar desconto de 10 por cento
    Então o valor com desconto deve ser 31.5

  Cenário: Pedido inválido sem endereço
    Dado que o usuário tem um carrinho vazio
    Quando adicionar "Sushi Combo" por 89.90
    E tentar finalizar o pedido sem endereço
    Então o pedido deve ser rejeitado
