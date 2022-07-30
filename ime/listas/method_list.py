minha_lista = []
minha_lista.append(5)
minha_lista.append(20)
minha_lista.append(7)
minha_lista.append(12)

print(minha_lista)

minha_lista.insert(2,47)
minha_lista.insert(4,47)
print(minha_lista)
print(minha_lista.count(47))  ## busca e conta o elemento passada da lista

print(minha_lista.index(7))
print(minha_lista.count(5))

minha_lista.reverse()
print(minha_lista)

ultimo_item = minha_lista.pop() ## remove o ultimo elemento da lista
print(ultimo_item)
print(minha_lista)

tirar_item = minha_lista.pop(2)
print(tirar_item)
print(minha_lista)

ordenada = minha_lista.sort()
print(ordenada)
print(minha_lista)

frutas = ['pera','laranja','banana','cereja']
for uma_fruta in frutas:
    print(uma_fruta)
print("*" * 10)
for pos in range(len(frutas)):
    print(frutas[pos])

print("*" * 30)
print()

for numero in range(21):
    if numero %3 ==0:
        print(numero)

print("*" * 30)
print()

numeros = [1,2,3,4,5]
print(numeros)

for i in range(len(numeros)):
    numeros[i] = numeros[i]**2

print(numeros)