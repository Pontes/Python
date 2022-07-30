def double_stuff(lista):

    """
    Recebe uma lista referenciada por lista e sobreescreve cada elemento da lista com o dobre do seu valor.
    """

    for posicao in range(len(lista)):
        lista[posicao] = 2 * lista[posicao]

coisas = [2,5,9]
print(coisas)
double_stuff(coisas)
print(coisas)