const validarLogin = require('../src/validarLogin')

describe('Função validarLogin', () => {

    test('deve validar login corretamente', () => {

        const resultado = validarLogin('admin', '123456')

        expect(resultado).toBe(true)
    })

    test('deve lançar erro para senha incorreta', () => {

        expect(() => {
            validarLogin('admin', '0000')
        }).toThrow('Usuário ou senha inválidos')
    })

    test('deve lançar erro para campos vazios', () => {

        expect(() => {
            validarLogin('', '')
        }).toThrow('Campos obrigatórios')
    })

})