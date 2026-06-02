from pathlib import Path
from playwright.sync_api import Page, expect


class BasePage:
    BASE_URL = "https://local-eats-unisenac.vercel.app/"
    INDEX_URL = "https://local-eats-unisenac.vercel.app/static/index.html"
    LOGIN_URL = "https://local-eats-unisenac.vercel.app/static/login.html"

    def __init__(self, page: Page):
        self.page = page
        self.corpo = page.locator("body")

    def acessar(self):
        """Prepara uma sessão válida e abre a página principal do LocalEats."""
        self.page.goto(self.LOGIN_URL, wait_until="domcontentloaded", timeout=60000)
        self.page.evaluate(
            """
            () => {
                localStorage.setItem('userId', '1');
                localStorage.setItem('userName', 'Lucas Fernandes da Silva');
            }
            """
        )
        self.page.goto(self.INDEX_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.corpo).to_be_visible(timeout=30000)

    def texto_da_pagina(self) -> str:
        return self.corpo.inner_text(timeout=30000)

    def validar_texto_na_pagina(self, texto: str):
        expect(self.corpo).to_contain_text(texto, timeout=30000)

    def tirar_print(self, nome_arquivo: str):
        pasta = Path("evidencias")
        pasta.mkdir(exist_ok=True)
        self.page.screenshot(path=str(pasta / f"{nome_arquivo}.png"), full_page=True)
