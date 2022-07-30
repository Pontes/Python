"""!
@mainpage Copia Texto
Esta atividade foi proposta no curso de **Engenharia de Software**
@section Disciplina
Laboratório de Progemação com Interfaces com o Usuário
@section Professor
André Saraiva
@author André Saraiva
@version 1.0
@date 17/03/2022
@copyright GNU Public Licence

Crie um programa que copie um arquivo texto.
Seu programa deverá abrir um arquivo texto,
ler linha a linha e escrever em outro arquivo
texto.


"""

def mostra(nome):
    infos = open(nome, "r")
    for linha in infos:
        print(linha.strip())
    infos.close()
    return None

def copiar(nomeOrigem, nomeDestino):
    orig = open(nomeOrigem, "r")
    dest = open(nomeDestino, "w")
    for linha in orig:
        dest.write(linha)
    orig.close()
    dest.close()
    return None

def main():
    nomes = input("Escreva os nomes dos arquivos, original e destino: ").split()
    mostra(nomes[0])
    copiar(nomes[0], nomes[1])
    mostra(nomes[1])

main()
