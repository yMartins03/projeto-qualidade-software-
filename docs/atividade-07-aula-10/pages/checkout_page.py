import re
from playwright.sync_api import Page, expect
from pages.carrinho_page import CarrinhoPage


class CheckoutPage(CarrinhoPage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _localizar_botao_finalizar(self):
        candidatos = [
            self.page.get_by_role("button", name=re.compile(r"finalizar", re.I)).first,
            self.page.locator("button").filter(has_text=re.compile(r"finalizar", re.I)).first,
            self.page.get_by_text(re.compile(r"finalizar pedido|checkout|concluir|enviar pedido", re.I)).first,
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
            "Não foi encontrado botão visível para finalizar o pedido. "
            "Texto atual da página: " + texto[:1000]
        ) from ultimo_erro

    def finalizar_pedido(self):
        self.adicionar_primeiro_item_ao_carrinho()
        botao = self._localizar_botao_finalizar()
        botao.scroll_into_view_if_needed(timeout=10000)
        botao.click(timeout=30000)
        expect(self.corpo).to_contain_text(
            re.compile(r"pedido|sucesso|finalizado|obrigado|confirmado", re.I),
            timeout=30000,
        )

    def validar_pedido_finalizado(self):
        expect(self.corpo).to_contain_text(
            re.compile(r"pedido|sucesso|finalizado|obrigado|confirmado", re.I),
            timeout=30000,
        )
