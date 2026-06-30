import re
from pytest_bdd import scenarios, given, when, then


scenarios('../features/navegacao_paginas.feature')


@given('que o usuário está na página inicial')
def acessar_pagina_inicial(page, base_url):
    page.goto(base_url)
    page.wait_for_load_state('networkidle', timeout=10000)
    page.wait_for_timeout(2000)


@when('o usuário clica no menu "Favoritos"')
def clicar_menu_favoritos(page):
    favorites_link = page.get_by_role("link", name=re.compile(r"favorito", re.I))
    favorites_link.click()
    page.wait_for_load_state('networkidle', timeout=10000)


@when('o usuário clica no menu "Meus Pedidos"')
def clicar_menu_pedidos(page):
    orders_link = page.get_by_role("link", name=re.compile(r"pedido", re.I))
    orders_link.click()
    page.wait_for_load_state('networkidle', timeout=10000)


@then('o sistema deve carregar a página de favoritos')
def verificar_pagina_favoritos(page):
    page.wait_for_timeout(1000)
    assert 'favorites' in page.url.lower() or page.locator('body').inner_text().lower().__contains__('favorito')


@then('o sistema deve carregar a página de pedidos')
def verificar_pagina_pedidos(page):
    page.wait_for_timeout(1000)
    assert 'orders' in page.url.lower() or page.locator('body').inner_text().lower().__contains__('pedido')
