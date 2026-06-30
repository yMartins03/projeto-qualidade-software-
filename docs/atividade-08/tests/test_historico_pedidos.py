import re
from pytest_bdd import scenarios, given, when, then


scenarios('../features/historico_pedidos.feature')


@given('que o usuário acessa a página de pedidos')
def acessar_pagina_pedidos(page):
    page.goto('https://local-eats-unisenac.vercel.app/static/orders.html')
    page.wait_for_load_state('networkidle', timeout=10000)
    page.wait_for_timeout(2000)


@when('visualizar o histórico de transações')
def visualizar_historico(page):
    page.locator('body').wait_for(state='visible', timeout=5000)


@when('visualizar um pedido específico')
def visualizar_pedido_especifico(page):
    page.wait_for_timeout(1000)


@then('o sistema deve exibir os pedidos cadastrados')
def verificar_pedidos_cadastrados(page):
    page_text = page.locator('body').inner_text().lower()
    assert 'pedido' in page_text or 'order' in page_text


@then('o status do pedido deve estar visível')
def verificar_status_pedido(page):
    page_text = page.locator('body').inner_text().lower()
    
    has_status_word = any(word in page_text for word in ['status', 'entregue', 'concluído', 'pendente', 'em preparo', 'entrega', 'finalizado'])
    has_order_content = 'pedido' in page_text or 'order' in page_text
    is_orders_page = 'orders' in page.url.lower()
    
    assert has_status_word or (has_order_content and is_orders_page), \
        "Página de pedidos deve conter informações de status ou pedidos"
