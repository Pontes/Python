x = []
num = float(input('insira um numero:'))
x.append(num)
for i in range(0,11):
    num = float(input('insira um numero:'))
    for j in x:
        if num > x[j]:
            aux = x[j]
            x.append(num)
            x.append(aux)
print(x)

