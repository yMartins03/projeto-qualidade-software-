import re
from playwright.sync_api import Page, expect
from pages.restaurantes_page import RestaurantesPage


class DetalhesRestaurantePage(RestaurantesPage):
    def __init__(self, page: Page):
        super().__init__(page)

    def acessar_detalhes_do_primeiro_restaurante(self):
        self.acessar()
        self.aguardar_lista()
        self.abrir_primeiro_restaurante()

    def validar_detalhes_visiveis(self):
        expect(self.corpo).to_contain_text(
            re.compile("cardápio|cardapio|menu|prato especial|adicionar|avaliações", re.I),
            timeout=30000,
        )

    def validar_itens_do_cardapio(self):
        expect(self.corpo).to_contain_text(
            re.compile(r"adicionar|prato especial|r\$|preço|preco", re.I),
            timeout=30000,
        )
