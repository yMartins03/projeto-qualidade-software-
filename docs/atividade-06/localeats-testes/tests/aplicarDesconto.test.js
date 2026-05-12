const aplicarDesconto = require('../src/aplicarDesconto')

describe('Função aplicarDesconto', () => {

    test('deve aplicar desconto corretamente', () => {
        const resultado = aplicarDesconto(100, 10)

        expect(resultado).toBe(90)
    })

    test('deve retornar mesmo valor quando desconto for 0%', () => {
        const resultado = aplicarDesconto(100, 0)

        expect(resultado).toBe(100)
    })

    test('deve lançar erro quando desconto for maior que 100%', () => {
        expect(() => {
            aplicarDesconto(100, 150)
        }).toThrow('Desconto inválido')
    })

})