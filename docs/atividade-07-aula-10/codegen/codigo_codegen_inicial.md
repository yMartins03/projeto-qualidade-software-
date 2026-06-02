# Registro do Codegen

Comando utilizado como ponto de partida:

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

## Exemplo de código bruto gerado

O Codegen gera comandos diretos, próximos do fluxo executado manualmente pelo usuário. Um exemplo de código inicial, antes da refatoração, ficou neste formato:

```python
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.get_by_role("button", name="Brasileira").click()
    page.locator(".restaurant-card").first.click()
    expect(page.locator("body")).to_contain_text("Cardápio")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
```

## Fluxos gravados

- Navegação pela página inicial e filtro de restaurantes.
- Abertura do primeiro restaurante da lista.
- Visualização das informações e do cardápio.
- Adição de item ao carrinho.
- Finalização do pedido.

## O que o Codegen fez bem

O Codegen ajudou a identificar a ordem correta das ações na interface, os cliques necessários e alguns seletores úteis, como botões e cards.

## O que o Codegen gerou de desnecessário

O código bruto ficou muito acoplado à interface. Ele também gerou comandos repetidos, alguns waits implícitos pouco claros e seletores que poderiam quebrar com pequenas mudanças visuais. Por isso, o código foi refatorado com Page Object Model.
