# def somaLista(numeros):
#     soma = 0
#     for i in numeros:
#         soma = soma + i
#     return soma
#
# print(somaLista([1,3,5,7,9]))
# print()
# print("============================")
# print()

def somaListaRec(numeros):
    if len(numeros)==1:
        return numeros[0]
    else:
        return numeros[0] + somaListaRec(numeros[1:])
print(somaListaRec([1,3,5,7,9,11]))


