quadrados = []
for x in range(1,11):
    quadrados.append(x*x)

print("quadrados 1", quadrados)

quadrados2 = [x*x for x in range(1,11)]
print("quadrados 2", quadrados2)