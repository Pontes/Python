palavra = 'Emanuelle'
for letra in palavra:
    #print(letra)
    if letra == 'a':
        print("Achou a letra a")


print("========================")
soma  = 0
for numero in range(1,6):
    soma = soma + numero
    print(soma)

print(soma)

print("========================")

for i in range(0,4):
    print(i)
    print('----------')
    for j in range(0,3):
        print(i,"->",j)
    print("++++++++++++")