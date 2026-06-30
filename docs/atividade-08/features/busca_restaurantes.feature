Funcionalidade: Busca de restaurantes

  Cenário: Busca válida retorna resultados
    Dado que o usuário está na página inicial
    Quando o usuário busca por "Pizza"
    Então o sistema deve exibir restaurantes relacionados

  Cenário: Busca inexistente retorna vazio
    Dado que o usuário está na página inicial
    Quando o usuário busca por "XYZABC123"
    Então o sistema não deve exibir restaurantes
