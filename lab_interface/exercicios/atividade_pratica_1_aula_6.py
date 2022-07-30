"""!
@mainpage Dict
Esta atividade foi proposta no curso de **Engenharia de Software**
@section Disciplina
Laboratório de Progemação com Interfaces com o Usuário
@section Professor
André Saraiva
@author André Saraiva
@version 1.0
@date 07/03/2022
@copyright GNU Public Licence

Crie um dicionário que faz a leitura de cinco nomes e telefones
e cria um dicionário com até cinco nomes distintos digitados pelo
usuário. Ocorre uma escrita do conteúdo do dicionário a cada
tentativa de inclusão de nome:fone 
"""

def dicionario():
    pares = dict() # ou pares = { }
    for i in range(5):
        nome = input("Digite nome: ")
        fone = input("Digite o telefone de "+nome+ ": ")
        pares[nome] = fone
    return (pares)

def main():
    myDict = dicionario()
    print(myDict)
    print(myDict.values())
    print(myDict.keys())

main()
