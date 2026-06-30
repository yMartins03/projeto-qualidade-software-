# Aula 12 – BDD e Automação Orientada a Comportamento

# Entrega PBL – LocalEats

**Disciplina**: Qualidade de Software  
**Instituição**: Centro Universitário Senac-RS  
**Sistema**: [LocalEats](https://local-eats-unisenac.vercel.app/)

---

## 👥 Integrantes

- Lucas Fernandes
- Henrique Laroque
- Adriel Martins
- Derick Laroque

---

# 🔹 1. Fluxo escolhido

## Integrante 1: Lucas Fernandes

### Fluxo

Busca de restaurantes

### Objetivo

Validar se a busca de restaurantes retorna resultados corretos.

---

## Integrante 2: Henrique Laroque

### Fluxo

Navegação entre páginas

### Objetivo

Validar se a navegação entre as seções do sistema funciona corretamente.

---

## Integrante 3: Adriel Martins

### Fluxo

Histórico de pedidos

### Objetivo

Validar se os pedidos realizados pelo usuário são exibidos corretamente.

---

## Integrante 4: Derick Laroque

### Fluxo

Visualização de restaurantes

### Objetivo

Validar se os restaurantes são exibidos corretamente na página inicial.

---

# 🔹 2. Cenários BDD

## Integrante 1 - Busca de Restaurantes

### Arquivo

```text
features/busca_restaurantes.feature
```

### Conteúdo

```gherkin
# language: pt
Feature: Busca de restaurantes

  Scenario: Busca válida retorna resultados
    Given que o usuário está na página inicial
    When o usuário busca por "Pizza"
    Then o sistema deve exibir restaurantes relacionados

  Scenario: Busca inexistente retorna vazio
    Given que o usuário está na página inicial
    When o usuário busca por "XYZABC123"
    Then o sistema não deve exibir restaurantes
```

---

## Integrante 2 - Navegação entre Páginas

### Arquivo

```text
features/navegacao_paginas.feature
```

### Conteúdo

```gherkin
# language: pt
Feature: Navegação entre páginas

  Scenario: Navegar para página de Favoritos
    Given que o usuário está na página inicial
    When o usuário clica no menu "Favoritos"
    Then o sistema deve carregar a página de favoritos

  Scenario: Navegar para página de Meus Pedidos
    Given que o usuário está na página inicial
    When o usuário clica no menu "Meus Pedidos"
    Then o sistema deve carregar a página de pedidos
```

---

## Integrante 3 - Histórico de Pedidos

### Arquivo

```text
features/historico_pedidos.feature
```

### Conteúdo

```gherkin
# language: pt
Feature: Histórico de pedidos

  Scenario: Visualizar pedidos realizados
    Given que o usuário acessa a página de pedidos
    When visualizar o histórico de transações
    Then o sistema deve exibir os pedidos cadastrados

  Scenario: Verificar status do pedido
    Given que o usuário acessa a página de pedidos
    When visualizar um pedido específico
    Then o status do pedido deve estar visível
```

---

## Integrante 4 - Visualização de Restaurantes

### Arquivo

```text
features/visualizacao_restaurantes.feature
```

### Conteúdo

```gherkin
# language: pt
Feature: Visualização de restaurantes

  Scenario: Visualizar cards de restaurantes
    Given que o usuário está na página inicial
    When a página é carregada
    Then o sistema deve exibir cards de restaurantes

  Scenario: Acessar detalhes de um restaurante
    Given que o usuário está na página inicial
    When o usuário clica em um restaurante
    Then o sistema deve abrir a página de detalhes
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
atividade-08/
│
├── features/
│   ├── busca_restaurantes.feature
│   ├── navegacao_paginas.feature
│   ├── historico_pedidos.feature
│   └── visualizacao_restaurantes.feature
│
├── tests/
│   ├── conftest.py
│   ├── test_busca_restaurantes.py
│   ├── test_navegacao_paginas.py
│   ├── test_historico_pedidos.py
│   └── test_visualizacao_restaurantes.py
│
├── evidencias/
│
└── README.md
```

---

## Exemplo de Automação

### Arquivo: `tests/conftest.py`

```python
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def base_url():
    return "https://local-eats-unisenac.vercel.app"
```

---

### Arquivo: `tests/test_historico_pedidos.py`

```python
from pytest_bdd import scenarios, given, when, then

scenarios('../features/historico_pedidos.feature')


@given('que o usuário acessa a página de pedidos')
def acessar_pagina(page, base_url):
    page.goto(f'{base_url}/static/orders.html')
    page.wait_for_load_state('networkidle')


@when('visualizar o histórico de transações')
def visualizar_historico(page):
    page.wait_for_selector('text=/histórico|transações/i')


@when('visualizar um pedido específico')
def visualizar_pedido(page):
    page.locator('.order-card, [class*="order"]').first.is_visible()


@then('o sistema deve exibir os pedidos cadastrados')
def validar_pedidos(page):
    orders = page.locator('.order-card, [class*="order"]')
    assert orders.count() > 0


@then('o status do pedido deve estar visível')
def validar_status(page):
    assert page.locator('text=/status|entregue|concluído/i').first.is_visible()
```

---

### Arquivo: `tests/test_busca_restaurantes.py`

```python
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/busca_restaurantes.feature')


@given('que o usuário está na página inicial')
def acessar_pagina(page, base_url):
    page.goto(base_url)
    page.wait_for_load_state('networkidle')


@when(parsers.parse('o usuário busca por "{termo}"'))
def buscar(page, termo):
    search = page.locator('input[type="text"], input[type="search"]').first
    search.fill(termo)
    page.keyboard.press('Enter')
    page.wait_for_timeout(1000)


@then('o sistema deve exibir restaurantes relacionados')
def validar_resultados(page):
    restaurants = page.locator('.restaurant-card, [class*="restaurant"]')
    assert restaurants.count() > 0


@then('o sistema não deve exibir restaurantes')
def validar_sem_resultados(page):
    restaurants = page.locator('.restaurant-card, [class*="restaurant"]')
    assert restaurants.count() == 0
```

---

# 🔹 4. Execução dos testes

## Comando executado

```bash
pytest -v
```

---

## Resultado da execução

```text
=================================================================== test session starts ====================================================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\deric\OneDrive\Área de Trabalho\qualidade de software\projeto-qualidade-software\docs\atividade-08\venv\Scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.14.3', 'Platform': 'Windows-11-10.0.26200-SP0', 'Packages': {'pytest': '9.0.3', 'pluggy': '1.6.0'}, 'Plugins': {'bdd': '8.1.0', 'html': '4.2.0', 'metadata': '3.1.1', 'xdist': '3.8.0'}}
rootdir: C:\Users\deric\OneDrive\Área de Trabalho\qualidade de software\projeto-qualidade-software\docs\atividade-08
configfile: pytest.ini
testpaths: tests
plugins: bdd-8.1.0, html-4.2.0, metadata-3.1.1, xdist-3.8.0
collected 8 items

tests/test_busca_restaurantes.py::test_busca_válida_retorna_resultados <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                        [ 12%]
tests/test_busca_restaurantes.py::test_busca_inexistente_retorna_vazio <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                        [ 25%]
tests/test_historico_pedidos.py::test_visualizar_pedidos_realizados <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                           [ 37%]
tests/test_historico_pedidos.py::test_verificar_status_do_pedido <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                              [ 50%]
tests/test_navegacao_paginas.py::test_navegar_para_página_de_favoritos <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                        [ 62%]
tests/test_navegacao_paginas.py::test_navegar_para_página_de_meus_pedidos <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                     [ 75%]
tests/test_visualizacao_restaurantes.py::test_visualizar_cards_de_restaurantes <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED                [ 87%]
tests/test_visualizacao_restaurantes.py::test_acessar_detalhes_de_um_restaurante <- venv\Lib\site-packages\pytest_bdd\scenario.py PASSED              [100%]

==================================================================== 8 passed in 52.93s ====================================================================
```

---

## Resumo

| Métrica            | Valor  |
| ------------------ | ------ |
| Total de cenários  | 8      |
| Cenários aprovados | 8 ✅   |
| Cenários falhados  | 0      |
| Tempo de execução  | 52.93s |
| Taxa de sucesso    | 100%   |

---

# 🔹 5. Evidências

## Logs da execução

A evidência completa da execução dos testes está documentada na seção 4 acima, mostrando:

- ✅ 8 cenários BDD executados com sucesso
- ✅ Cobertura dos 4 fluxos escolhidos (busca, navegação, histórico, visualização)
- ✅ Tempo total de execução: 52.93 segundos
- ✅ 100% de aprovação nos testes automatizados

---

# 🔹 6. Análise crítica

## O cenário escrito ficou compreensível?

Sim. A estrutura Given-When-Then deixou claro o comportamento esperado do sistema.

---

## O teste automatizado ficou legível?

Sim. Os steps estão bem nomeados e as funções são autoexplicativas.

---

## O BDD ajudou a entender o comportamento?

Sim. Os cenários descrevem o que o sistema faz sem entrar em detalhes técnicos de implementação.

---

## Quais dificuldades surgiram?

- Identificar seletores estáveis no LocalEats
- Integrar pytest-bdd com Playwright corretamente
- Lidar com timeouts e esperas de elementos
- Estruturar os steps de forma reutilizável

---

## Os seletores foram frágeis?

Sim. Muitos elementos não possuem IDs ou data-testid, então foi necessário usar seletores por classe ou texto, que podem quebrar facilmente.

---

## O teste ficou dependente da interface?

Sim. Mudanças no HTML ou CSS podem quebrar os testes, pois os seletores dependem da estrutura atual.

---

## O cenário representa realmente uma regra de negócio?

Parcialmente. Alguns cenários focam mais em funcionalidades técnicas (como navegação) do que em regras de negócio puras.

---

## O que tornaria o teste mais robusto?

- Usar atributos data-testid nos elementos
- Implementar Page Object Pattern
- Criar esperas mais inteligentes
- Controlar os dados de teste
- Separar ambientes (dev, staging, prod)

---

# 🔹 7. Reflexão no contexto do LocalEats

## BDD melhora comunicação entre equipe?

Sim. Os cenários escritos em linguagem natural facilitam o entendimento entre QA, desenvolvimento e stakeholders.

---

## Todo teste deve ser escrito em BDD?

Não. BDD é mais adequado para testes de aceitação e fluxos importantes do negócio. Testes unitários e de integração técnicos não precisam de BDD.

---

## Quando vale a pena usar BDD?

Vale a pena quando:

- Há múltiplos stakeholders envolvidos
- O comportamento precisa estar documentado
- Os requisitos não estão totalmente claros
- É necessário validação de negócio

---

## O comportamento ficou mais claro?

Sim. Antes os requisitos eram vagos, agora temos cenários concretos e executáveis.

---

## Como isso ajuda no projeto do grupo?

- Alinha expectativas entre os membros da equipe
- Cria documentação executável
- Facilita identificação de gaps nos requisitos
- Permite testes de regressão automatizados
- Melhora a comunicação sobre funcionalidades

---

# 📦 Repositório GitHub

```text
https://github.com/yMartins03/projeto-qualidade-software-
```

---

# ✅ Conclusão

A atividade permitiu compreender:

- Escrita de cenários BDD em linguagem natural
- Automação orientada a comportamento com pytest-bdd
- Integração entre pytest-bdd e Playwright
- Importância da legibilidade dos testes
- Desafios na manutenção de automações de frontend
- Valor do BDD na comunicação entre equipes

O BDD mostrou-se uma abordagem valiosa para transformar requisitos em testes executáveis e compreensíveis por toda a equipe.

---

**Data de entrega**: Junho de 2026  
**Disciplina**: Qualidade de Software - Senac-RS
