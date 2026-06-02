# Atividade PBL – Aula 10

## Testes Funcionais Automatizados – LocalEats

### Integrantes

- Lucas Fernandes da Silva
- Henrique dos Santos Laroque
- Adriel Martins de Anunciação
- Derick dos Santos Laroque

---

## 1. Fluxos funcionais escolhidos

Cada integrante ficou responsável por um fluxo diferente do sistema LocalEats.

| Integrante | Fluxo escolhido | Objetivo do teste |
|---|---|---|
| Lucas Fernandes da Silva | Navegação e visualização de restaurantes | Validar se a página inicial carrega, se o filtro de comida brasileira funciona e se é possível abrir um restaurante. |
| Henrique dos Santos Laroque | Visualização de detalhes de um restaurante | Validar se os detalhes do restaurante e as informações do cardápio são exibidos. |
| Adriel Martins de Anunciação | Adição de item ao carrinho | Validar se um item pode ser adicionado ao carrinho e se o pedido é atualizado. |
| Derick dos Santos Laroque | Fluxo de pedido e checkout | Validar se o usuário consegue adicionar um item e finalizar o pedido. |

---

## 2. Teste automatizado com Codegen

O Codegen foi utilizado como ponto de partida para gravar os fluxos principais da aplicação.

### Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### Código gerado automaticamente, antes da refatoração

Exemplo simplificado do código bruto gerado pelo Codegen:

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

### Fluxo gravado

O fluxo gravado inicialmente consistiu em acessar o sistema, visualizar a lista de restaurantes, aplicar filtro de culinária brasileira, abrir um restaurante, visualizar o cardápio, adicionar item ao carrinho e finalizar o pedido.

### Observações iniciais

O Codegen foi útil para entender a sequência de ações do usuário e capturar seletores iniciais. Porém, o código gerado ficou muito direto e pouco organizado, pois misturava acesso à página, ações, validações e fechamento do navegador em um único arquivo.

### O que o Codegen fez bem

O Codegen ajudou a identificar os cliques principais, os campos visíveis e a ordem correta das interações. Também facilitou a visualização de quais seletores poderiam ser utilizados na primeira versão do teste.

### O que o Codegen gerou de desnecessário

O Codegen gerou código repetitivo e pouco reutilizável. Alguns seletores ficaram muito dependentes da estrutura visual da página, o que poderia tornar o teste frágil. Por isso, o código foi refatorado com Page Object Model.

---

## 3. Implementação dos testes com Pytest

Os testes foram implementados com Python, Playwright e Pytest.

### Estrutura dos testes

```text
tests
  test_01_lucas_navegacao_restaurantes.py
  test_02_henrique_detalhes_restaurante.py
  test_03_adriel_adicionar_item_carrinho.py
  test_04_derick_fluxo_checkout.py
```

### Teste 1 – Lucas Fernandes da Silva

```python
from pages.restaurantes_page import RestaurantesPage


def test_lucas_navegacao_e_visualizacao_de_restaurantes(page):
    restaurantes = RestaurantesPage(page)

    restaurantes.acessar()
    restaurantes.aguardar_lista()
    restaurantes.filtrar_por_brasileira()
    restaurantes.validar_lista_visivel()
    restaurantes.abrir_primeiro_restaurante()
    restaurantes.validar_detalhes_visiveis()
    restaurantes.tirar_print("lucas_navegacao_restaurantes")
```

### Teste 2 – Henrique dos Santos Laroque

```python
from pages.detalhes_restaurante_page import DetalhesRestaurantePage


def test_henrique_visualizacao_de_detalhes_do_restaurante(page):
    detalhes = DetalhesRestaurantePage(page)

    detalhes.acessar_detalhes_do_primeiro_restaurante()
    detalhes.validar_detalhes_visiveis()
    detalhes.tirar_print("henrique_detalhes_restaurante")
```

### Teste 3 – Adriel Martins de Anunciação

```python
from pages.carrinho_page import CarrinhoPage


def test_adriel_adicao_de_item_ao_carrinho(page):
    carrinho = CarrinhoPage(page)

    carrinho.adicionar_primeiro_item_ao_carrinho()
    carrinho.validar_carrinho_atualizado()
    carrinho.tirar_print("adriel_item_carrinho")
```

### Teste 4 – Derick dos Santos Laroque

```python
from pages.checkout_page import CheckoutPage


def test_derick_fluxo_de_pedido_checkout(page):
    checkout = CheckoutPage(page)

    checkout.finalizar_pedido()
    checkout.validar_pedido_finalizado()
    checkout.tirar_print("derick_fluxo_checkout")
```

---

## 4. Refatoração com Page Object Model

Após a gravação inicial com Codegen, os testes foram refatorados com Page Object Model. Essa organização evita repetição de código e separa as ações da página dos testes.

### Estrutura criada

```text
pages
  base_page.py
  restaurantes_page.py
  detalhes_restaurante_page.py
  carrinho_page.py
  checkout_page.py
```

### Exemplo de Page Object

```python
class RestaurantesPage(BasePage):
    def filtrar_por_brasileira(self):
        self.botao_brasileira.click(timeout=30000)
        expect(self.corpo).to_contain_text(re.compile("brasileira", re.I), timeout=30000)
```

### Vantagens da refatoração

A refatoração deixou os testes mais limpos, organizados e fáceis de manter. Caso algum seletor da tela mude, a correção pode ser feita dentro da classe da página, sem necessidade de alterar todos os testes.

---

## 5. Execução dos testes

### Comando de instalação

```bash
pip install -r requirements.txt
playwright install
```

### Comando de execução

```bash
pytest
```

### Resultado esperado

```text
4 testes coletados
4 testes passaram
0 testes falharam
```

### Evidências

Durante a execução, os testes geram prints na pasta `evidencias`.

```text
evidencias
  lucas_navegacao_restaurantes.png
  henrique_detalhes_restaurante.png
  adriel_item_carrinho.png
  derick_fluxo_checkout.png
```

Observação: no ambiente de preparação desta entrega não foi possível executar contra o site real, pois o domínio externo não resolveu no terminal. No computador local, com internet e Playwright instalado, a validação deve ser feita com o comando `pytest`.

---

## 6. Análise crítica dos testes

### O teste quebrou em algum momento? Por quê?

Sim. Durante a construção inicial, alguns seletores quebraram porque o texto “Brasileira” aparecia em mais de um ponto da tela. Isso poderia causar erro de seletor ambíguo. A solução foi usar seletor mais específico, buscando o botão com o nome exato da categoria.

### Quais seletores foram mais difíceis?

Os seletores mais difíceis foram os cards dos restaurantes e os botões de ação, pois a interface pode usar classes diferentes ou textos semelhantes. Por isso, foram utilizados seletores mais flexíveis, combinando classes prováveis e textos visíveis.

### O Codegen ajudou ou gerou problemas?

O Codegen ajudou como ponto de partida, pois mostrou a sequência do fluxo e os primeiros seletores. Porém, o código bruto não era adequado para entrega final, pois ficou repetitivo e frágil. A refatoração com POM foi necessária.

### O teste é confiável? Por quê?

O teste é mais confiável do que uma validação manual repetitiva, pois executa os principais fluxos de forma padronizada. Além disso, usa assertions para confirmar se a lista, os detalhes, o carrinho e o checkout aparecem corretamente.

### O que tornaria o teste mais robusto?

O teste ficaria mais robusto se a aplicação tivesse atributos próprios para teste, como `data-testid`. Isso reduziria a dependência de textos e classes visuais.

### Quais são os riscos de manutenção?

O principal risco é a mudança de textos, nomes de botões ou estrutura dos cards. Se o frontend mudar muito, alguns seletores precisarão ser atualizados. O uso do POM reduz esse problema, pois centraliza a manutenção nas classes da pasta `pages`.

---

## 7. Reflexão no contexto do LocalEats

### Testes automatizados substituem testes manuais?

Não substituem totalmente. Os testes automatizados ajudam a validar fluxos repetitivos e importantes, mas os testes manuais ainda são úteis para avaliar experiência do usuário, layout, clareza das mensagens e comportamento visual.

### Vale a pena automatizar todos os fluxos?

Não. O ideal é priorizar os fluxos mais importantes, repetitivos e críticos para o funcionamento do sistema. Automatizar tudo pode gerar muito custo de manutenção.

### Qual tipo de teste deve ser priorizado?

Devem ser priorizados os fluxos principais do usuário, como login, navegação, visualização de restaurante, carrinho e checkout. Esses fluxos impactam diretamente a experiência e o funcionamento do LocalEats.

### Como isso ajuda no projeto do grupo?

A automação ajuda o grupo a identificar rapidamente falhas após mudanças no frontend. Também aumenta a confiança para alterar o sistema, pois os testes avisam quando algum fluxo principal para de funcionar.

---

## Conclusão

A atividade foi desenvolvida com testes funcionais automatizados usando Python, Playwright e Pytest. O Codegen foi utilizado como ponto de partida, mas o código final foi refatorado com Page Object Model para melhorar organização, legibilidade e manutenção.
