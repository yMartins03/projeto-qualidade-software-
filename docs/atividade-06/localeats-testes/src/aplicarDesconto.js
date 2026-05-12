function aplicarDesconto(valorTotal, desconto) {

    if (desconto < 0 || desconto > 100) {
        throw new Error('Desconto inválido')
    }

    const valorDesconto = valorTotal * (desconto / 100)

    return valorTotal - valorDesconto
}

module.exports = aplicarDesconto