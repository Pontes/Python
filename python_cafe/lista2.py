
def busca(lista, elem):
    """Retorna o indice do elemente se ele estiver na lista ou None, caso não esteja na lista"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


lista_exemplo = [8,'5', 32,0,"python",11]
elemento = 32


indice = busca(lista_exemplo, elemento)
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento,indice))
else:
    print("o elemento {} não se encontra na lista". format(elemento))