tupla = ('Homo sapiens', 'Canis familiaris', 'Felix catus')
print(tupla)
print(tupla[1])
print(tupla.index('Canis familiaris'))

lista1 = ['Homo sapiens', 'Canis familiaris', 'Felix catus']
lista2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

lista3 = lista1 + lista2
## junção de listas
print("Lista3 {}".format(lista3))
## multiplicando os elementos da lista -  repetição
print(lista2 * 2)
print(lista1[0])
## exibir apenas uma quantidade de elementos de uma lista
print(lista3[0:2])
## adicionar um elemento a lista
lista1.append('Gorila gorila')
print(lista1)
lista1.remove('Felix catus')
print(lista1)
##comando para apagar uma lista
##del(lista1)
##print(lista1)

for item in lista3:
    print(item)

#######################
## Dicionários

coleta = {'Aedes aegyt': 32, 'Aedes albopictus': 22, 'anopheles darlingi': 14}
print(coleta['Aedes aegyt'])


