# Aula 09 — Testes Unitários Automatizados e TDD — LocalEats

## Disciplina
Qualidade de Software

---

# 1. Objetivo da atividade

Aplicar testes unitários automatizados e a pratica de TDD (Red → Green → Refactor) em regras de negocio do sistema LocalEats.

---

# 2. Ferramenta utilizada

- Node.js
- Jest
- JavaScript

---

# 3. Estrutura do projeto

```txt
src/
tests/
package.json
```

---

# 4. Funcionalidades implementadas

Cada integrante implementou uma regra de negocio diferente:

- Adriel Martins → Taxa de entrega
- Henrique Laroque → Desconto percentual
- Lucas Fernandes → Total do pedido
- Derick Laroque → Validacao de login

---

# 5. Aplicacao do TDD (exemplo: calculo de taxa de entrega)

## Red

O teste foi escrito antes da funcao existir. Ao rodar o Jest nesse momento, o teste falha por ausencia da implementacao.

```js
test('deve retornar taxa fixa para distancia ate 3km', () => {
    const resultado = calcularTaxaEntrega(2)

    expect(resultado).toBe(5)
})
```

## Green

Foi criada a implementacao minima para fazer o teste passar.

```js
function calcularTaxaEntrega(distancia) {
    if (distancia < 0) {
        throw new Error('Distancia invalida')
    }

    const TAXA_FIXA = 5
    const KM_LIMITE = 3
    const VALOR_KM_EXCEDENTE = 2

    if (distancia <= KM_LIMITE) {
        return TAXA_FIXA
    }

    const kmExcedente = distancia - KM_LIMITE

    return TAXA_FIXA + (kmExcedente * VALOR_KM_EXCEDENTE)
}
```

## Refactor

Depois foram feitas melhorias sem quebrar os testes:

- Uso de constantes para taxas e limites.
- Validacao explicita de distancia negativa.
- Separacao do calculo do excedente para legibilidade.

---

# 6. Testes unitarios

Cada teste abaixo inclui nome, cenario, entradas, resultado esperado e o codigo do teste.

## 6.1. Aplicacao de desconto percentual

### Teste 1

- Nome: deve aplicar desconto corretamente
- Cenario: desconto valido sobre o total
- Entradas: valorTotal = 100, desconto = 10
- Resultado esperado: 90

```js
test('deve aplicar desconto corretamente', () => {
    const resultado = aplicarDesconto(100, 10)

    expect(resultado).toBe(90)
})
```

### Teste 2

- Nome: deve retornar mesmo valor quando desconto for 0%
- Cenario: desconto zero
- Entradas: valorTotal = 100, desconto = 0
- Resultado esperado: 100

```js
test('deve retornar mesmo valor quando desconto for 0%', () => {
    const resultado = aplicarDesconto(100, 0)

    expect(resultado).toBe(100)
})
```

### Teste 3

- Nome: deve lancar erro quando desconto for maior que 100%
- Cenario: desconto invalido
- Entradas: valorTotal = 100, desconto = 150
- Resultado esperado: erro 'Desconto invalido'

```js
test('deve lancar erro quando desconto for maior que 100%', () => {
    expect(() => {
        aplicarDesconto(100, 150)
    }).toThrow('Desconto invalido')
})
```

## 6.2. Calculo de taxa de entrega

### Teste 1

- Nome: deve retornar taxa fixa para distancia ate 3km
- Cenario: distancia dentro do limite
- Entradas: distancia = 2
- Resultado esperado: 5

```js
test('deve retornar taxa fixa para distancia ate 3km', () => {
    const resultado = calcularTaxaEntrega(2)

    expect(resultado).toBe(5)
})
```

### Teste 2

- Nome: deve calcular taxa proporcional acima de 3km
- Cenario: distancia acima do limite
- Entradas: distancia = 5
- Resultado esperado: 9

```js
test('deve calcular taxa proporcional acima de 3km', () => {
    const resultado = calcularTaxaEntrega(5)

    expect(resultado).toBe(9)
})
```

### Teste 3

- Nome: deve lancar erro para distancia negativa
- Cenario: distancia invalida
- Entradas: distancia = -1
- Resultado esperado: erro 'Distancia invalida'

```js
test('deve lancar erro para distancia negativa', () => {
    expect(() => {
        calcularTaxaEntrega(-1)
    }).toThrow('Distancia invalida')
})
```

## 6.3. Calculo do total do pedido

### Teste 1

- Nome: deve calcular corretamente o total do pedido
- Cenario: soma dos itens acima do minimo
- Entradas: itens = [{ preco: 10 }, { preco: 20 }], valorMinimo = 15
- Resultado esperado: 30

```js
test('deve calcular corretamente o total do pedido', () => {
    const itens = [
        { preco: 10 },
        { preco: 20 }
    ]

    const resultado = calcularTotalPedido(itens, 15)

    expect(resultado).toBe(30)
})
```

### Teste 2

- Nome: deve aceitar pedido exatamente no valor minimo
- Cenario: soma exatamente no minimo
- Entradas: itens = [{ preco: 10 }, { preco: 5 }], valorMinimo = 15
- Resultado esperado: 15

```js
test('deve aceitar pedido exatamente no valor minimo', () => {
    const itens = [
        { preco: 10 },
        { preco: 5 }
    ]

    const resultado = calcularTotalPedido(itens, 15)

    expect(resultado).toBe(15)
})
```

### Teste 3

- Nome: deve lancar erro quando valor minimo nao for atingido
- Cenario: soma abaixo do minimo
- Entradas: itens = [{ preco: 5 }, { preco: 5 }], valorMinimo = 20
- Resultado esperado: erro 'Valor minimo nao atingido'

```js
test('deve lancar erro quando valor minimo nao for atingido', () => {
    const itens = [
        { preco: 5 },
        { preco: 5 }
    ]

    expect(() => {
        calcularTotalPedido(itens, 20)
    }).toThrow('Valor minimo nao atingido')
})
```

## 6.4. Validacao de login

### Teste 1

- Nome: deve validar login corretamente
- Cenario: credenciais corretas
- Entradas: usuario = 'admin', senha = '123456'
- Resultado esperado: true

```js
test('deve validar login corretamente', () => {
    const resultado = validarLogin('admin', '123456')

    expect(resultado).toBe(true)
})
```

### Teste 2

- Nome: deve lancar erro para senha incorreta
- Cenario: senha invalida
- Entradas: usuario = 'admin', senha = '0000'
- Resultado esperado: erro 'Usuario ou senha invalidos'

```js
test('deve lancar erro para senha incorreta', () => {
    expect(() => {
        validarLogin('admin', '0000')
    }).toThrow('Usuario ou senha invalidos')
})
```

### Teste 3

- Nome: deve lancar erro para campos vazios
- Cenario: entradas vazias
- Entradas: usuario = '', senha = ''
- Resultado esperado: erro 'Campos obrigatorios'

```js
test('deve lancar erro para campos vazios', () => {
    expect(() => {
        validarLogin('', '')
    }).toThrow('Campos obrigatorios')
})
```

---

# 7. Execucao dos testes

Total de testes: 12
Passaram: 12
Falharam: 0

Evidencia (Jest):

```txt
PASS  tests/validarLogin.test.js
PASS  tests/aplicarDesconto.test.js
PASS  tests/calcularTotalPedido.test.js
PASS  tests/calcularTaxaEntrega.test.js

Test Suites: 4 passed, 4 total
Tests:       12 passed, 12 total
Snapshots:   0 total
Time:        0.525 s, estimated 1 s
Ran all test suites.
```

---

# 8. Reflexao

Foi dificil escrever testes antes do codigo?

Sim, porque exige pensar primeiro no comportamento esperado do sistema e nas regras de negocio.

O TDD ajudou no desenvolvimento?

Sim, porque orientou o passo a passo e evitou implementar algo fora do que os testes pediam.

Os testes aumentaram a confianca no codigo?

Sim, porque toda alteracao pode ser validada rapidamente e reduz o risco de regressao.

O que poderia melhorar?

Adicionar mais cenarios de borda, como valores nulos, tipos invalidos e itens sem preco.

Como isso ajuda no projeto?

Facilita manutencao, evita regressao e melhora a confiabilidade das regras de negocio.
