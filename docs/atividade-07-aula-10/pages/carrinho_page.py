import re
from playwright.sync_api import Page, expect
from pages.detalhes_restaurante_page import DetalhesRestaurantePage


class CarrinhoPage(DetalhesRestaurantePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.indicador_carrinho = page.get_by_text(re.compile("carrinho|pedido|total|finalizar", re.I)).first

    def _localizar_botao_adicionar(self):
        """Localiza o botão real de adicionar item dentro da tela de detalhes."""
        candidatos = [
            self.page.get_by_role("button", name=re.compile(r"adicionar", re.I)).first,
            self.page.locator("button").filter(has_text=re.compile(r"adicionar", re.I)).first,
            self.page.locator("button").filter(has_text=re.compile(r"\+", re.I)).first,
            self.page.locator("text=/\\+\\s*Adicionar/i").first,
            self.page.locator("text=/Adicionar/i").first,
        ]

        ultimo_erro = None
        for candidato in candidatos:
            try:
                candidato.wait_for(state="visible", timeout=7000)
                return candidato
            except Exception as erro:
                ultimo_erro = erro

        texto = self.texto_da_pagina()
        raise AssertionError(
            "Não foi encontrado botão visível para adicionar item ao carrinho. "
            "Texto atual da página: " + texto[:1000]
        ) from ultimo_erro

    def adicionar_primeiro_item_ao_carrinho(self):
        self.acessar_detalhes_do_primeiro_restaurante()

        expect(self.corpo).to_contain_text(
            re.compile(r"cardápio|cardapio|prato especial", re.I),
            timeout=30000,
        )

        aba_cardapio = self.page.get_by_role("button", name=re.compile(r"cardápio|cardapio", re.I)).first
        try:
            aba_cardapio.click(timeout=3000)
        except Exception:
            pass

        botao = self._localizar_botao_adicionar()
        botao.scroll_into_view_if_needed(timeout=10000)
        botao.click(timeout=30000)

        expect(self.corpo).to_contain_text(
            re.compile(r"seu pedido|carrinho|pedido|total|item|finalizar", re.I),
            timeout=30000,
        )

    def validar_carrinho_atualizado(self):
        expect(self.corpo).to_contain_text(
            re.compile(r"seu pedido|carrinho|pedido|total|item|finalizar", re.I),
            timeout=30000,
        )
