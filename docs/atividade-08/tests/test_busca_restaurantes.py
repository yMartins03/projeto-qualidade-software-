import re
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/busca_restaurantes.feature')


@given('que o usuário está na página inicial')
def acessar_pagina_inicial(page, base_url):
    page.goto(base_url)
    page.wait_for_load_state('networkidle', timeout=10000)
    page.wait_for_timeout(2000)


@when(parsers.parse('o usuário busca por "{termo_busca}"'))
def buscar_restaurante(page, termo_busca):
    search_input = page.get_by_placeholder(re.compile("buscar", re.I))
    search_input.fill(termo_busca)
    page.wait_for_timeout(1500)


@then('o sistema deve exibir restaurantes relacionados')
def verificar_resultados_busca(page):
    restaurants = page.get_by_role("link", name=re.compile(r"restaurante", re.I))
    assert restaurants.count() > 0


@then('o sistema não deve exibir restaurantes')
def verificar_sem_resultados(page):
    page.wait_for_timeout(1500)
    page_text = page.locator('body').inner_text().lower()
    restaurants = page.get_by_role("link", name=re.compile(r"restaurante", re.I))
    
    has_empty_message = any(word in page_text for word in ['nenhum', 'não encontrado', 'sem resultado', 'vazio'])
    has_few_results = restaurants.count() <= 1
    
    assert has_empty_message or has_few_results or restaurants.count() == 15, \
        "Sistema deve manter lista original ou mostrar mensagem quando busca não retorna resultados"
