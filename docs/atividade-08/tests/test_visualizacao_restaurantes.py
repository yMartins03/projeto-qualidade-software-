import re
from pytest_bdd import scenarios, given, when, then


scenarios('../features/visualizacao_restaurantes.feature')


@given('que o usuário está na página inicial')
def acessar_pagina_inicial(page, base_url):
    page.goto(base_url)
    page.wait_for_load_state('networkidle', timeout=10000)
    page.wait_for_timeout(2000)


@when('a página é carregada')
def aguardar_carregamento(page):
    page.wait_for_timeout(2000)


@when('o usuário clica em um restaurante')
def clicar_restaurante(page):
    restaurant = page.get_by_role("link", name=re.compile(r"restaurante", re.I)).first
    restaurant.click()
    page.wait_for_load_state('networkidle', timeout=10000)


@then('o sistema deve exibir cards de restaurantes')
def verificar_cards_restaurantes(page):
    restaurants = page.get_by_role("link", name=re.compile(r"restaurante", re.I))
    assert restaurants.count() > 0


@then('o sistema deve abrir a página de detalhes')
def verificar_pagina_detalhes(page):
    page.wait_for_timeout(2000)
    page_text = page.locator('body').inner_text().lower()
    assert any(word in page_text for word in ['cardápio', 'cardapio', 'menu', 'prato', 'adicionar'])
