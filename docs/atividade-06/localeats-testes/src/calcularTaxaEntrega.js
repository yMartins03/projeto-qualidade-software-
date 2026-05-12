function calcularTaxaEntrega(distancia) {

    if (distancia < 0) {
        throw new Error("Distância inválida")
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

module.exports = calcularTaxaEntrega