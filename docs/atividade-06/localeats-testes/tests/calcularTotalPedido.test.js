const calcularTotalPedido = require('../src/calcularTotalPedido')

describe('Função calcularTotalPedido', () => {

    test('deve calcular corretamente o total do pedido', () => {

        const itens = [
            { preco: 10 },
            { preco: 20 }
        ]

        const resultado = calcularTotalPedido(itens, 15)

        expect(resultado).toBe(30)
    })

    test('deve aceitar pedido exatamente no valor mínimo', () => {

        const itens = [
            { preco: 10 },
            { preco: 5 }
        ]

        const resultado = calcularTotalPedido(itens, 15)

        expect(resultado).toBe(15)
    })

    test('deve lançar erro quando valor mínimo não for atingido', () => {

        const itens = [
            { preco: 5 },
            { preco: 5 }
        ]

        expect(() => {
            calcularTotalPedido(itens, 20)
        }).toThrow('Valor mínimo não atingido')
    })

})