nome = input("Digite o seu nome: ")
matricula = input("Digite a sua matricula")
cad_pessoafisica = input("Qual seu CPF: ")

eu = [nome, matricula, cad_pessoafisica]

n_nome = eu[0]
n_mat = eu[1]

print(n_nome[:3]," - ", n_mat[-3:])

