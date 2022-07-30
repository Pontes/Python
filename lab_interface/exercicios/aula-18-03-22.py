from random import randint

def minhalista(elem, qtd, menor, maior):
    for item in range(qtd):
        elem.append(randint(menor, maior))
    return None

def removerDuplicados(elem):
    indice = 0
    while indice<len(elem):
        if elem.count(elem[indice])==1:
            indice +=1
        else:
            elem.remoce(elem[indice])
    return None

def main():
    lista =[]
    qtd = int(input('digite a quantidade: '))
    menor = int(input('digite o menor valor: '))
    maior = int(input('digite o maior valor: '))
    minhalista(lista, qtd, menor,maior)
    print
    removerDuplicados(lista)
    print(sorted(lista))

main()
