import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RestaurantesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.campo_busca = page.get_by_placeholder(re.compile("buscar", re.I))
        self.botao_todos = page.get_by_role("button", name=re.compile("^todos$", re.I))
        self.botao_brasileira = page.get_by_role("button", name=re.compile("^brasileira$", re.I))
        self.carregando = page.get_by_text(re.compile("carregando", re.I))
        self.links_restaurantes = page.get_by_role("link", name=re.compile(r"restaurante sabor", re.I))
        self.cards_restaurantes = page.locator(
            ", ".join(
                [
                    ".restaurant-card",
                    ".restaurante-card",
                    "[data-testid*='restaurant']",
                    "[data-testid*='restaurante']",
                    "article",
                    "a:has-text('Restaurante Sabor')",
                    ".card:has-text('Restaurante Sabor')",
                ]
            )
        )

    def aguardar_pagina_inicial(self):
        expect(self.corpo).to_be_visible(timeout=30000)
        expect(self.corpo).to_contain_text(re.compile("buscar", re.I), timeout=30000)
        expect(self.corpo).to_contain_text(re.compile("todos", re.I), timeout=30000)
        expect(self.corpo).to_contain_text(re.compile("brasileira", re.I), timeout=30000)

    def aguardar_lista(self):
        self.aguardar_pagina_inicial()
        try:
            self.carregando.wait_for(state="hidden", timeout=20000)
        except Exception:
            pass
        expect(self.primeiro_restaurante()).to_be_visible(timeout=30000)

    def primeiro_restaurante(self):
        """Retorna o primeiro restaurante clicável da lista."""
        if self.links_restaurantes.count() > 0:
            return self.links_restaurantes.first
        return self.cards_restaurantes.first

    def filtrar_por_brasileira(self):
        self.botao_brasileira.click(timeout=30000)
        expect(self.corpo).to_contain_text(re.compile("brasileira", re.I), timeout=30000)

    def quantidade_de_cards(self) -> int:
        quantidade_links = self.links_restaurantes.count()
        if quantidade_links > 0:
            return quantidade_links
        return self.cards_restaurantes.count()

    def validar_lista_visivel(self):
        self.aguardar_lista()
        assert self.quantidade_de_cards() > 0, "A lista de restaurantes deveria exibir pelo menos um card."

    def validar_detalhes_visiveis(self):
        expect(self.corpo).to_contain_text(
            re.compile("cardápio|cardapio|menu|prato|adicionar|restaurante", re.I),
            timeout=30000,
        )

    def abrir_primeiro_restaurante(self):
        self.aguardar_lista()
        primeiro = self.primeiro_restaurante()
        expect(primeiro).to_be_visible(timeout=30000)
        primeiro.scroll_into_view_if_needed(timeout=10000)
        primeiro.click(timeout=30000)

        try:
            self.page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            pass

        expect(self.corpo).to_contain_text(
            re.compile(r"cardápio|cardapio|prato especial|\+\s*adicionar|avaliações", re.I),
            timeout=30000,
        )
