biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidratos', 'lipídeos', 'ácidos nucleicos', 'carboidratos', 'carboidratos', 'carboidratos')
print(biomoleculas)
print('representação de conjuntos')
print(set(biomoleculas))

print()
c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)
print('Diferenças', c1.difference(c2))
print("diferença c2 para c1", c2.difference(c1))