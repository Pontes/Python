alunos = {'Pedro':8.0,'Maria':10.0,'Amilton':7.5}

with open('notas.txt','w') as notas:
    for nome, nota in alunos.items():
        notas.write(f'{nome},{nota}\n')
    notas.close()

with open('notas.txt','r') as notas:

    for leitura in notas:
        print(leitura)
    notas.close()
