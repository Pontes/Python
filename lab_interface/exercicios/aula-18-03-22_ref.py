from random import randint
lista = []

qtd = int(input('digite a quantidade: '))
menor = int(input('digite o menor valor: '))
maior = int(input('digite o maior valor: '))

lt = []
while True:
    x = randint(menor, maior)
    if x <= maior or x >= menor:
        lista.append(x)
        if len(lista) == qtd:
            break
lt = sorted(lista)
print(lt)
