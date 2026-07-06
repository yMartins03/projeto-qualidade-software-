# Aula 17 - Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

# Entrega PBL - LocalEats

**Disciplina**: Qualidade de Software  
**Instituição**: Centro Universitário Senac-RS  
**Sistema**: [LocalEats](https://local-eats-unisenac.vercel.app/)  
**Repositório do grupo**: [projeto-qualidade-software-](https://github.com/yMartins03/projeto-qualidade-software-)  
**Repositório da atividade**: [projeto-qualidade-software](https://github.com/LarroqueD/projeto-qualidade-software)

---

## Integrantes

- Lucas Fernandes
- Henrique Laroque
- Adriel Martins
- Derick Laroque

---

# 1. Repositório da Atividade

| Item                | Descrição                                               |
| ------------------- | ------------------------------------------------------- |
| Nome do repositório | `projeto-qualidade-software`                            |
| Link do repositório | https://github.com/LarroqueD/projeto-qualidade-software |

**Estrutura de diretórios:**

```
atividade-12/
├── .gitignore
├── .github/
│   └── workflows/
│       └── quality.yml
├── features/
│   └── calculo_pedido.feature
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_calculo_pedido.py
│   └── test_calculo_pedido_bdd.py
├── localeats.py
├── pytest.ini
└── requirements.txt
```

---

# 2. Planejamento da Funcionalidade

| Item                       | Descrição                                                                                                                                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Título da Issue            | `[Feature] Implementar cálculo e validação de pedido no carrinho`                                                                                                                                                  |
| Objetivo da funcionalidade | Permitir que o usuário adicione itens ao carrinho, calcule o total, aplique descontos e valide o pedido antes de finalizar, garantindo que o carrinho não esteja vazio e que o endereço de entrega seja informado. |
| Link da Issue              | https://github.com/LarroqueD/projeto-qualidade-software/issues/1                                                                                                                                                   |

---

# 3. Teste Automatizado

| Item                         | Descrição                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Tipo de teste                | Unitário + BDD                                                                                                                                  |
| Objetivo do teste            | Verificar que as regras de cálculo de total, aplicação de desconto e validação de pedido funcionam corretamente em todos os cenários esperados. |
| Link para o arquivo do teste | [tests/test_calculo_pedido.py](tests/test_calculo_pedido.py) · [tests/test_calculo_pedido_bdd.py](tests/test_calculo_pedido_bdd.py)             |

**Código dos testes unitários (`test_calculo_pedido.py`):**

```python
"""
Testes Unitários – Cálculo e validação de pedido no LocalEats
Atividade 12 – Aula 17: Integração Contínua e Qualidade Automatizada
"""
import pytest
from localeats import ItemPedido, Carrinho, validar_pedido


class TestItemPedido:

    def test_subtotal_quantidade_unitaria(self):
        item = ItemPedido("Pizza", 45.90)
        assert item.subtotal() == 45.90

    def test_subtotal_multipla_quantidade(self):
        item = ItemPedido("Suco", 8.50, quantidade=3)
        assert item.subtotal() == 25.50

    def test_preco_negativo_lanca_excecao(self):
        with pytest.raises(ValueError, match="Preço não pode ser negativo"):
            ItemPedido("Combo", -10.0)

    def test_quantidade_zero_lanca_excecao(self):
        with pytest.raises(ValueError, match="Quantidade deve ser maior que zero"):
            ItemPedido("Combo", 10.0, quantidade=0)


class TestCarrinho:

    def test_carrinho_vazio_total_zero(self):
        carrinho = Carrinho()
        assert carrinho.calcular_total() == 0.0

    def test_carrinho_vazio_esta_vazio(self):
        carrinho = Carrinho()
        assert carrinho.esta_vazio() is True

    def test_adicionar_item_atualiza_total(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza Margherita", 45.90))
        assert carrinho.calcular_total() == 45.90

    def test_adicionar_multiplos_itens(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        carrinho.adicionar_item(ItemPedido("Refrigerante", 7.00))
        assert carrinho.calcular_total() == 52.90

    def test_quantidade_itens_correta(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        carrinho.adicionar_item(ItemPedido("Salada", 18.00))
        assert carrinho.quantidade_itens() == 2

    def test_aplicar_desconto_10_porcento(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Hambúrguer", 35.00))
        assert carrinho.aplicar_desconto(10) == 31.50

    def test_aplicar_desconto_zero(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Sushi", 89.90))
        assert carrinho.aplicar_desconto(0) == 89.90

    def test_desconto_negativo_lanca_excecao(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Sushi", 89.90))
        with pytest.raises(ValueError, match="Percentual de desconto deve estar entre 0 e 100"):
            carrinho.aplicar_desconto(-5)

    def test_desconto_acima_100_lanca_excecao(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Sushi", 89.90))
        with pytest.raises(ValueError, match="Percentual de desconto deve estar entre 0 e 100"):
            carrinho.aplicar_desconto(110)


class TestValidarPedido:

    def test_pedido_valido(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        resultado = validar_pedido(carrinho, "Rua das Flores, 123")
        assert resultado["valido"] is True
        assert resultado["erros"] == []

    def test_pedido_sem_itens_invalido(self):
        carrinho = Carrinho()
        resultado = validar_pedido(carrinho, "Rua das Flores, 123")
        assert resultado["valido"] is False
        assert "Carrinho não pode estar vazio" in resultado["erros"]

    def test_pedido_sem_endereco_invalido(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        resultado = validar_pedido(carrinho, "")
        assert resultado["valido"] is False
        assert "Endereço de entrega é obrigatório" in resultado["erros"]

    def test_pedido_endereco_apenas_espacos_invalido(self):
        carrinho = Carrinho()
        carrinho.adicionar_item(ItemPedido("Pizza", 45.90))
        resultado = validar_pedido(carrinho, "   ")
        assert resultado["valido"] is False
        assert "Endereço de entrega é obrigatório" in resultado["erros"]
```

**Código do teste BDD (`features/calculo_pedido.feature`):**

```gherkin
# language: pt
Funcionalidade: Cálculo de pedido no LocalEats

  Como usuário do LocalEats
  Quero calcular o total do meu carrinho
  Para saber o valor antes de finalizar o pedido

  Cenário: Carrinho vazio tem total zero
    Dado que o usuário tem um carrinho vazio
    Então o total do carrinho deve ser 0.0

  Cenário: Adicionar item atualiza o total
    Dado que o usuário tem um carrinho vazio
    Quando adicionar "Pizza Margherita" por 45.90
    Então o total do carrinho deve ser 45.9

  Cenário: Aplicar desconto de 10 por cento
    Dado que o usuário tem um carrinho vazio
    Quando adicionar "Hambúrguer Artesanal" por 35.00
    E aplicar desconto de 10 por cento
    Então o valor com desconto deve ser 31.5

  Cenário: Pedido inválido sem endereço
    Dado que o usuário tem um carrinho vazio
    Quando adicionar "Sushi Combo" por 89.90
    E tentar finalizar o pedido sem endereço
    Então o pedido deve ser rejeitado
```

**Código de automação BDD (`test_calculo_pedido_bdd.py`):**

```python
"""
Testes BDD – Cálculo de pedido no LocalEats
Atividade 12 – Aula 17: Integração Contínua e Qualidade Automatizada
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from localeats import ItemPedido, Carrinho, validar_pedido


scenarios('../features/calculo_pedido.feature')


@pytest.fixture
def contexto():
    return {"carrinho": None, "desconto_aplicado": None, "resultado_pedido": None}


@given("que o usuário tem um carrinho vazio", target_fixture="contexto")
def carrinho_vazio():
    return {"carrinho": Carrinho(), "desconto_aplicado": None, "resultado_pedido": None}


@when(parsers.parse('adicionar "{nome}" por {preco:f}'))
def adicionar_item(contexto, nome, preco):
    contexto["carrinho"].adicionar_item(ItemPedido(nome, preco))


@when(parsers.parse("aplicar desconto de {percentual:d} por cento"))
def aplicar_desconto(contexto, percentual):
    contexto["desconto_aplicado"] = contexto["carrinho"].aplicar_desconto(percentual)


@when("tentar finalizar o pedido sem endereço")
def finalizar_sem_endereco(contexto):
    contexto["resultado_pedido"] = validar_pedido(contexto["carrinho"], "")


@then(parsers.parse("o total do carrinho deve ser {total:f}"))
def verificar_total(contexto, total):
    assert contexto["carrinho"].calcular_total() == pytest.approx(total, abs=0.01)


@then(parsers.parse("o valor com desconto deve ser {valor:f}"))
def verificar_desconto(contexto, valor):
    assert contexto["desconto_aplicado"] == pytest.approx(valor, abs=0.01)


@then("o pedido deve ser rejeitado")
def pedido_rejeitado(contexto):
    resultado = contexto["resultado_pedido"]
    assert resultado["valido"] is False
    assert "Endereço de entrega é obrigatório" in resultado["erros"]
```

---

# 4. Pipeline de Integração Contínua

| Item                             | Descrição                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------- |
| Nome do workflow                 | `Quality Check – LocalEats`                                                      |
| Evento que dispara a execução    | `push` nas branches `main` e `develop`; `pull_request` na branch `main`          |
| Link para o arquivo do workflow  | [.github/workflows/quality.yml](.github/workflows/quality.yml)                   |
| Link de uma execução do workflow | https://github.com/LarroqueD/projeto-qualidade-software/actions/runs/28758067865 |

**Código do workflow (`quality.yml`):**

```yaml
name: Quality Check – LocalEats

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    name: Testes Automatizados e Qualidade
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do repositório
        uses: actions/checkout@v4

      - name: Configurar Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Executar testes com relatório JUnit
        run: |
          pytest tests/ -v --tb=short --junitxml=test-results.xml

      - name: Publicar resultados dos testes
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: test-results.xml
```

---

# 5. Indicadores de Qualidade

> Indicadores coletados após execução local com `python -m pytest tests/ -v --tb=short`  
> (os mesmos resultados são reproduzidos no pipeline do GitHub Actions)

| Indicador                       | Valor                             |
| ------------------------------- | --------------------------------- |
| Quantidade de testes executados | 21                                |
| Quantidade de testes aprovados  | 21                                |
| Quantidade de testes com falha  | 0                                 |
| Status final do pipeline        | ✅ Sucesso (`21 passed in 0.07s`) |

**Composição dos testes:**

| Arquivo                      | Tipo     | Testes |
| ---------------------------- | -------- | ------ |
| `test_calculo_pedido.py`     | Unitário | 17     |
| `test_calculo_pedido_bdd.py` | BDD      | 4      |
| **Total**                    |          | **21** |

---

# 6. Registro de Defeito

| Item              | Descrição                                                                    |
| ----------------- | ---------------------------------------------------------------------------- |
| Título do defeito | `[Bug] Desconto acima de 100% não lança exceção – total pode ficar negativo` |
| Severidade        | Alta                                                                         |
| Link da Issue     | https://github.com/LarroqueD/projeto-qualidade-software/issues/2             |

**Descrição do defeito:**

- **Qual foi o defeito?** Na versão inicial de `Carrinho.aplicar_desconto()`, não havia validação do percentual informado. Um valor como `150` resultava em total negativo, o que é inaceitável em um sistema de pagamentos.
- **Como ele foi identificado?** Durante a escrita dos testes unitários `test_desconto_negativo_lanca_excecao` e `test_desconto_acima_100_lanca_excecao`, o método não lançava exceção e os testes falharam, evidenciando a ausência da regra de negócio.
- **Como foi corrigido?** Adicionada validação `if percentual < 0 or percentual > 100: raise ValueError(...)` no início do método, seguida de re-execução do pipeline para confirmar que todos os 21 testes voltaram a passar com status verde.
