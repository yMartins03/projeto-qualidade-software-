const calcularTaxaEntrega = require('../src/calcularTaxaEntrega')

describe('Função calcularTaxaEntrega', () => {

    test('deve retornar taxa fixa para distância até 3km', () => {
        const resultado = calcularTaxaEntrega(2)

        expect(resultado).toBe(5)
    })

    test('deve calcular taxa proporcional acima de 3km', () => {
        const resultado = calcularTaxaEntrega(5)

        expect(resultado).toBe(9)
    })

    test('deve lançar erro para distância negativa', () => {
        expect(() => {
            calcularTaxaEntrega(-1)
        }).toThrow('Distância inválida')
    })

})