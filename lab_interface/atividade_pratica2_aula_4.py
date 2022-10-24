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

Imprima na saída padrão (vídeo) os resultados de uma turma de
cinco alunos com três provas cada. Sua aplicação deverá imprimir
a matriz de entrada “alunos” e a matriz de entrada ‘resultados”.
Em seguida deverá imprimir se o aluno(a) foi aprovado ou não.

alunos = [“Maria”, “Lucas”, “Ana”, “Juca”, “Carlos”]

resultados = [ [7.2, 4.5, 6.1], [3.3, 8.5, 4.5], [7.8, 6.7, 8.3],
             [4.0, 6.0, 9.2], [2.3, 3.4, 4.0] ] 

"""

def listaAprovadosReprovados(estudantes, notas, minimo):
    for pos in range(len(estudantes)):
        media = (notas[pos][0]+notas[pos][1]+notas[pos][2])/3
        if media>=minimo:
            print(estudantes[pos], "Aprovado com nota: %4.2f" % media)
    print("---------------------------------------------------------------")
    for pos in range(len(estudantes)):
        media = (notas[pos][0]+notas[pos][1]+notas[pos][2])/3
        if media<minimo:
            print(estudantes[pos], "Reprovado com nota: %4.2f" % media)
    return None

def main(): 
    alunos = ["Maria", "Lucas", "Ana", "Juca", "Carlos"]
    resultados = [ [7.2, 4.5, 6.1], [3.3, 8.5, 4.5], [7.8, 6.7, 8.3], [4.0, 6.0, 9.2], [2.3, 3.4, 4.0] ]
    print(alunos)
    print(resultados)
    listaAprovadosReprovados(alunos, resultados, 6.0)

main()
