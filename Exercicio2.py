def calcular_media_avaliacoes(filmes):
    soma_avaliacoes = sum(filme['avaliacao'] for filme in filmes)
    return soma_avaliacoes / len(filmes)

def calcular_filme_melhor_avaliado(filmes):
    melhor_nota = max(filme['avaliacao'] for filme in filmes)
    melhor_filme = ''
    for filme in filmes:
        if filme['avaliacao'] == melhor_nota:
            melhor_filme = filme['titulo']
    return melhor_filme

def ano_filme_pior_avaliado(filmes):
    pior_nota = min(filme['avaliacao'] for filme in filmes)
    ano_filme = 0
    for filme in filmes:
        if filme['avaliacao'] == pior_nota:
            ano_filme = filme['ano']
    return ano_filme



filmes = [
    {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
    {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
    {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]

media_avaliacoes = calcular_media_avaliacoes(filmes)
print(media_avaliacoes)
filme_melhor_avaliado = calcular_filme_melhor_avaliado(filmes)
print(filme_melhor_avaliado)
ano_pior_filme = ano_filme_pior_avaliado(filmes)
print(ano_pior_filme)