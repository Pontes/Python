dcn = {}
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = input("Digite a nota do aluno: ")
    dcn[nome] = nota
print("Alunos e notas: ", dcn)
print(dcn['maria'])
print(dcn.values())

notas = 0
for nome1, nota1 in dcn.items():
    notas = float(nota1) + notas

media = notas/3
print(f'Média geral dos alunos {media}')
