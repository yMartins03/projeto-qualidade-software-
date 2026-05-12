function validarLogin(usuario, senha) {

    if (!usuario || !senha) {
        throw new Error('Campos obrigatórios')
    }

    const usuarioSistema = 'admin'
    const senhaSistema = '123456'

    if (usuario !== usuarioSistema || senha !== senhaSistema) {
        throw new Error('Usuário ou senha inválidos')
    }

    return true
}

module.exports = validarLogin