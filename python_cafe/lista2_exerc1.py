
def busca(lista, elem):

    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

lista = []

for i in range(0,10):
    elemento = input("Digite um elemento para lista: ")
    lista.append(elemento)

valorx = input("digite um elemento para buscar na lista:")
indice = busca(lista,valorx)

if indice is not None:
    print("O índice do elemento {} é {}".format(valorx, indice))
else:
    print("o elemento {} não se encontra na lista".format(valorx))