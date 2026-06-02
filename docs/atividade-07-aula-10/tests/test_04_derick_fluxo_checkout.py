from pages.checkout_page import CheckoutPage


def test_derick_fluxo_de_pedido_checkout(page):
    checkout = CheckoutPage(page)

    checkout.finalizar_pedido()
    checkout.validar_pedido_finalizado()
    checkout.tirar_print("derick_fluxo_checkout")
