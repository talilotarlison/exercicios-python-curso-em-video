# Retorna None caso não encontre ou a posição, caso encontre.
# https://pt.wikipedia.org/wiki/Busca_linear

def procura(lista, elemento):
    assert isinstance(lista, list)
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    else:
        return None
