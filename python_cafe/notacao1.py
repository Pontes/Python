' função que inverter uma lista'

def inverter_lista(lista):
    nova_lista = []
    tamanho = len(lista)
    print(tamanho)
    for i in range(tamanho):
        nova_lista = lista[tamanho-i]
    return nova_lista

lista = [1,3,5,7,9,11]

print(lista)

print("invertendo lista...")

inverter_lista(lista)
