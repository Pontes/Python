lista = []

for i in range(2):
    x = float(input('digite um numero decimal: '))
    lista.append(x)

try:
    divisao = lista[0]/lista[1]
except ZeroDivisionError:
    print("Não é Possível divisão por zero! ou insira")
    print("*** tente Novamente ***")
    break
except IndexError:
    print("não existe valor para ser dividido nessa posição da lista")
    print("*** tente Novamente ***")
    break
except KeyboardInterrupt:
    print("Execução interrompida pelo usuário!")
    break
else:
    print(f'O resultado da divisão é: {divisao}')
    break