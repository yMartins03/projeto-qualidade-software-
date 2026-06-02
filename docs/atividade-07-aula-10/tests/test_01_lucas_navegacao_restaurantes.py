from pages.restaurantes_page import RestaurantesPage


def test_lucas_navegacao_e_visualizacao_de_restaurantes(page):
    restaurantes = RestaurantesPage(page)

    restaurantes.acessar()
    restaurantes.aguardar_lista()
    restaurantes.filtrar_por_brasileira()
    restaurantes.validar_lista_visivel()
    restaurantes.abrir_primeiro_restaurante()
    restaurantes.validar_detalhes_visiveis()
    restaurantes.tirar_print("lucas_navegacao_restaurantes")
