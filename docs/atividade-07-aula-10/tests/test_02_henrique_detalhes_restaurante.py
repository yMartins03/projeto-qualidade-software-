from pages.detalhes_restaurante_page import DetalhesRestaurantePage


def test_henrique_visualizacao_de_detalhes_do_restaurante(page):
    detalhes = DetalhesRestaurantePage(page)

    detalhes.acessar_detalhes_do_primeiro_restaurante()
    detalhes.validar_detalhes_visiveis()
    detalhes.tirar_print("henrique_detalhes_restaurante")
