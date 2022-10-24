lista = []
# for i in range(5):
#     num = int(input("Digite um número inteiro: "))
#     lista.append(num)

# x = 0
# for i in range(len(lista)):
#     x = lista[i] + x
# print(f'a soma da lista é {x}')


"""
Refatorando o exercicio
"""
x= 0
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
    x = num + x

print(f'a soma dos valores é {x}')

