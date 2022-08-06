a = ['um','dois','tres']
del a[1]
print(a)

lista = ["a","b","c","d","e","f"]
del lista[1:5]
print(lista)

lista_original = [45,76,34,55]
lista_nova = [lista_original] * 3
print(lista_nova)
lista_original[1]=99
print(lista_nova)