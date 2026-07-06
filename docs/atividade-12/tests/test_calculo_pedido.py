"""
Testes Unitários – Cálculo e validação de pedido no LocalEats
Atividade 12 – Aula 17: Integração Contínua e Qualidade Automatizada
"""
import pytest
from localeats import ItemPedido, Carrinho, validar_pedido


# ──────────────────────────────────────────────
# ItemPedido
# ──────────────────────────────────────────────

class TestItemPedido:

    def test_subtotal_quantidade_unitaria(self):
        item = ItemPedido("Pizza", 45.90)
        assert item.subtotal() == 45.90

    def test_subtotal_multipla_quantidade(self):
        item = ItemPedido("Suco", 8.50, quantidade=3)
        assert item.subtotal() == 25.50

    def test_preco_negativo_lanca_excecao(self):
        with pytest.raises(ValueError, match="Preço não pode ser negativo"):
            ItemPedido("Combo", -10.0)

    def test_quantidade_zero_lanca_excecao(self):
        with pytest.raises(ValueError, match="Quantidade deve ser maior que zero"):
            ItemPedido("Combo", 10.0, quantidade=0)


# ──────────────────────────────────────────────
# Carrinho
# ──────────────────────────────────────────────

class TestCarrinho:

    def test_carrinho_vazio_total_zero(self):
        carrinho = Carrinho()
        assert carrinho.calcular_total() == 0.0

    def test_carrinho_vazio_esta_vazio(self):
        carrinho = Carrinho()
        assert carrinho.esta_vazio() is True

    def test_adicionar_item_atualiza_total(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza Margherita", 45.90))
        assert carrinho.calcular_total() == 45.90

    def test_adicionar_multiplos_itens(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        carrinho.adicionar_item(ItemPedido("Refrigerante", 7.00))
        assert carrinho.calcular_total() == 52.90

    def test_quantidade_itens_correta(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        carrinho.adicionar_item(ItemPedido("Salada", 18.00))
        assert carrinho.quantidade_itens() == 2

    def test_aplicar_desconto_10_porcento(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Hambúrguer", 35.00))
        assert carrinho.aplicar_desconto(10) == 31.50

    def test_aplicar_desconto_zero(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Sushi", 89.90))
        assert carrinho.aplicar_desconto(0) == 89.90

    def test_desconto_negativo_lanca_excecao(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Sushi", 89.90))
        with pytest.raises(ValueError, match="Percentual de desconto deve estar entre 0 e 100"):
            carrinho.aplicar_desconto(-5)

    def test_desconto_acima_100_lanca_excecao(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Sushi", 89.90))
        with pytest.raises(ValueError, match="Percentual de desconto deve estar entre 0 e 100"):
            carrinho.aplicar_desconto(110)


# ──────────────────────────────────────────────
# validar_pedido
# ──────────────────────────────────────────────

class TestValidarPedido:

    def test_pedido_valido(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        resultado = validar_pedido(carrinho, "Rua das Flores, 123")
        assert resultado["valido"] is True
        assert resultado["erros"] == []

    def test_pedido_sem_itens_invalido(self):
        carrinho = Carrinho()
        resultado = validar_pedido(carrinho, "Rua das Flores, 123")
        assert resultado["valido"] is False
        assert "Carrinho não pode estar vazio" in resultado["erros"]

    def test_pedido_sem_endereco_invalido(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        resultado = validar_pedido(carrinho, "")
        assert resultado["valido"] is False
        assert "Endereço de entrega é obrigatório" in resultado["erros"]

    def test_pedido_endereco_apenas_espacos_invalido(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        resultado = validar_pedido(carrinho, "   ")
        assert resultado["valido"] is False
        assert "Endereço de entrega é obrigatório" in resultado["erros"]
