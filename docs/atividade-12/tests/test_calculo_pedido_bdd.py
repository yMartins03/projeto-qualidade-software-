"""
Testes BDD – Cálculo de pedido no LocalEats
Atividade 12 – Aula 17: Integração Contínua e Qualidade Automatizada
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from localeats import ItemPedido, Carrinho, validar_pedido


scenarios('../features/calculo_pedido.feature')


# ──────────────────────────────────────────────
# Fixtures de contexto
# ──────────────────────────────────────────────

@pytest.fixture
def contexto():
    return {"carrinho": None, "desconto_aplicado": None, "resultado_pedido": None}


# ──────────────────────────────────────────────
# Given
# ──────────────────────────────────────────────

@given("que o usuário tem um carrinho vazio", target_fixture="contexto")
def carrinho_vazio():
    return {"carrinho": Carrinho(), "desconto_aplicado": None, "resultado_pedido": None}


# ──────────────────────────────────────────────
# When
# ──────────────────────────────────────────────

@when(parsers.parse('adicionar "{nome}" por {preco:f}'))
def adicionar_item(contexto, nome, preco):
    contexto["carrinho"].adicionar_item(ItemPedido(nome, preco))


@when(parsers.parse("aplicar desconto de {percentual:d} por cento"))
def aplicar_desconto(contexto, percentual):
    contexto["desconto_aplicado"] = contexto["carrinho"].aplicar_desconto(percentual)


@when("tentar finalizar o pedido sem endereço")
def finalizar_sem_endereco(contexto):
    contexto["resultado_pedido"] = validar_pedido(contexto["carrinho"], "")


# ──────────────────────────────────────────────
# Then
# ──────────────────────────────────────────────

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
