#3=4 ## erro de sintaxe

# print('Meu Nome é ', nome) ## variavel não definida NameError

# print(3/0) ## ZeroDivisionError divisão por zero

# c = [1,2,3,4,5]
# print(c[5]) ## IndexError: erro fora da lista

# while True:
#     try:
#         n = int(input("Digite um número inteiro: "))
#     except:
#         print('Valor inválido')
#     else:
#         print(f'Valor digitado é: ', n)
#         break

while True:
    try:
        p = int(input('Digite um número inteiro: '))
except ValueError:
        print("valor inválido!")
    except KeyboardInterrupt:
        print("Usuário interrompeu a execução!")
        break
    else:
        print(f'Valor digitado é :', p)
        break