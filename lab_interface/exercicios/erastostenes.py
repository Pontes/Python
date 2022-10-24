"""!
@mainpage Crivo de Eratóstenes
Esta atividade foi proposta no curso de **Engenharia de Software**
@section Disciplina
LaboratÃ³rio de ProgemaÃ§Ã£o com Interfaces com o UsuÃ¡rio
@section Professor
AndrÃ© Saraiva
@author AndrÃ© Saraiva
@version 1.0
@date 07/03/2022
@copyright GNU Public Licence

Este programa gera e imprime os números primos entre 2 e N,
escolhido pelo usuário, usando o algoritmo chamado de
“Crivo de Eratóstenes”

"""

def imprime(num, osPrimos):
    print("Primos entre 2 e", num, ":")
    for candidato in range(2, num+1):
        if candidato in osPrimos:
            print(candidato, end=" ")
    print()
    return None

def eratostenes(num):
    resposta = set() # inicializa resposta
    vazio = set() # inicializa conjunto vazio
    crivo = set(range(2, num+1)) # constrói conjunto de 2 a num
    prox = 2
    while crivo != vazio:
        while not (prox in crivo):
            prox += 1
        resposta.add(prox) 
        j = prox
        while j <= num:
            crivo.discard(j) 
            j += prox
    return resposta

def main():
    n = int(input("Escolha o valor de N: "))
    primos = eratostenes(n)
    imprime(n, primos)

main()
