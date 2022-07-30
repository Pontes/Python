"""!
@mainpage Ordena Reais
Esta atividade foi proposta no curso de **Engenharia de Software**
@section Disciplina
Laboratório de Progemação com Interfaces com o Usuário
@section Professor
André Saraiva
@author André Saraiva
@version 1.0
@date 07/03/2022
@copyright GNU Public Licence

Faça um programa para ler, do teclado, dez números reais.
Após a inserção dos números, deverá ser escrito, na saída
padrão (vídeo), a listagem de entrada e em ordem crescente.

"""

def escrever(valores):
    ## for que varre cada item do vetor valores
    for item in valores:
        print(item, end="")
        print()
    return None

def ler(valores):
    ## for que faz a inserção de cada elemento no vetor valores
    for ind in range(len(valores)):
        valores[ind] = float(input("s["+str(ind+1)+"] = "))
    return None

def ordenar(valores):
    ## algoritmo de ordenação
    def ondeMenor(vals, inicio):
        posMenor = inicio
        for p in range(inicio+1, len(vals)):
            if vals[p]<vals[posMenor]:
                posMenor = p
        return posMenor
    for ind in range(len(valores)-1):
        posicao = ondeMenor(valores, ind)
        temp = valores[ind]
        valores[ind] = valores[posicao]
        valores[posicao] = temp
    return None


def main():
    TAM = 10
    numeros = [0.0]*TAM
    ler(numeros)
    print("Numeros Digitados")
    escrever(numeros)
    ordenar(numeros)
    print("Numeros Ordenados")
    escrever(numeros)

main()
