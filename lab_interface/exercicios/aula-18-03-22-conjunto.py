escolhidos = set()
escolhidos.add(13)
print(escolhidos)

conjunto = {20,11,68,93}
print(len(conjunto))
conjunto.discard(68)
print(conjunto)

"""
conjA = set()
for i in range(5):
    nome = input("digite o nome: ")
    conjA.add(nome)
    print(conjA)
    """

nome = {"maria", "Ana", "Giovanna", "Leandro", "Dante"}
print(nome)

## union de conjuntos
x = {1,3,5,7}.union({2,3,4,6,7,8})
y = {1,3,5,7}.intersection({2,3,4,6,7,8})
z = y = {1,3,5,7}.difference({2,3,4,6,7,8})
print("union: ",x)
print("intersection: ",y)
print("difference: ",y)

ano = {'jan', 'fev','mar', 'abr','maio','jun','jul','ago','set','out', 'nov','dez'}
feriasFimAno = {'jan', 'fev','dez'}
feriasMeioAno = {'jul'}
ferias = feriasFimAno.union(feriasMeioAno)
periodoLetivo = ano.difference(ferias)
print("ferias ", ferias)
print("ano letivo: ", periodoLetivo)

print("*******************************")

