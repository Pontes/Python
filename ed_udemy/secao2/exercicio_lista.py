import numpy as np
lista =[]
for i in range(5):
    num =  int(input("Digite um número: "))
    lista.append(num)
print(lista)

soma = 0
for x in lista:
    soma = x + soma
print(soma)
print("*"*10)

print(np.array(lista).sum())
