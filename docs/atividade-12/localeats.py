"""
LocalEats - Módulo de lógica de negócio para cálculo e validação de pedidos.
Utilizado nos testes automatizados da Atividade 12 - Aula 17.
"""


class ItemPedido:
    """Representa um item adicionado ao carrinho."""

    def __init__(self, nome: str, preco: float, quantidade: int = 1):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return round(self.preco * self.quantidade, 2)


class Carrinho:
    """Representa o carrinho de compras do usuário."""

    def __init__(self):
        self.itens: list[ItemPedido] = []

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)

    def remover_item(self, nome: str):
        self.itens = [i for i in self.itens if i.nome != nome]

    def calcular_total(self) -> float:
        return round(sum(item.subtotal() for item in self.itens), 2)

    def aplicar_desconto(self, percentual: float) -> float:
        if percentual < 0 or percentual > 100:
            raise ValueError("Percentual de desconto deve estar entre 0 e 100")
        total = self.calcular_total()
        desconto = total * (percentual / 100)
        return round(total - desconto, 2)

    def quantidade_itens(self) -> int:
        return len(self.itens)

    def esta_vazio(self) -> bool:
        return len(self.itens) == 0


def validar_pedido(carrinho: Carrinho, endereco: str) -> dict:
    """Valida se um pedido pode ser finalizado."""
    erros = []
    if carrinho.esta_vazio():
        erros.append("Carrinho não pode estar vazio")
    if not endereco or not endereco.strip():
        erros.append("Endereço de entrega é obrigatório")
    return {"valido": len(erros) == 0, "erros": erros}
