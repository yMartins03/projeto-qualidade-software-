from pages.carrinho_page import CarrinhoPage


def test_adriel_adicao_de_item_ao_carrinho(page):
    carrinho = CarrinhoPage(page)

    carrinho.adicionar_primeiro_item_ao_carrinho()
    carrinho.validar_carrinho_atualizado()
    carrinho.tirar_print("adriel_item_carrinho")
