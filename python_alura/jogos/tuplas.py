ponto = (3,5)
print(ponto)
p1 = (3,5)
p2 = (4,6)
p3 = (5,7)

linha =[p1, p2, p3]
print(linha)

inst1 = ("Nico", 39)
inst2 = ("Pontes", 37)

instrutores = [inst1, inst2]
print(instrutores)
print(instrutores[0])
print(instrutores[0][0])
print(f'Instrutor: {instrutores[0][0]} tem idade {instrutores[0][1]}')

## aqui pegar uma lista e transformar em tuplas
palavras =[]
palavras.append("banana")
palavras.append("morango")
nova = tuple(palavras)
print(nova)

professores = {'Pontes Junior':42, 'Brendon': 18}
print("professor: ",professores['Pontes Junior'])



