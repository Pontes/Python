#como criar e modificar arquivos:
valoresCelulares = [850,2230,1500,3500,5000]
'''
'r' -> usado somente para ler algo
'w' -> usado somente para escrever
'r+' -> usado para ler e escrever algo
'a' -> usado para acrescentar algo
'''

# with open('valores_celulares.txt','w') as arquivo:
#     for valor in valoresCelulares:
#         arquivo.write(str(valor)+ '\n')

# with open('valores_celulares.txt','a') as arquivo:
#     for valor in valoresCelulares:
#         arquivo.write(str(valor)+ '\n')
#
# with open('valores_celulares.txt','r') as arquivo:
#     for valor in valoresCelulares:
#         print(valor)

# with open('valores_celulares.txt','r') as arquivo:
#     for valor in arquivo:
#         print(valor)

with open('valores_celulares.txt', 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')

