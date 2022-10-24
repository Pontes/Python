"""!
@mainpage Lista
Esta atividade foi proposta no curso de **Engenharia de Software**
@section Disciplina
Laboratório de Progemação com Interfaces com o Usuário
@section Professor
André Saraiva
@author André Saraiva
@version 1.0
@date 07/03/2022
@copyright GNU Public Licence

Criando uma lista de números com quantidade de números
aleatórios e um intervalo de valores escolhidos pelo usuário.

"""
from random import randint


def preencher(listaElems, qtd, min, max):
    for item in range(qtd):
        listaElems.append(randint(min,max))
    return None

def main():
    qtdNumeros = int(input("A Lista deve ter quantos valores?: "))
    minimo = int(input("Menor valor da faixa: "))
    maximo = int(input("Maior valor da faixa: "))
    numeros = [ ]
    preencher(numeros, qtdNumeros, minimo, maximo)
    print(numeros)

main()
