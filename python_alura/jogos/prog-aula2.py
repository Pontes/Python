def imprimirValor(i):
    print("o valor é: {}".format(i))

def ent_num(quantidade):
    for i in range(1,quantidade+1):
        lista.append(int(input("digite um numero: ")))
    menu()

def imprimeLista():
    for i in lista:
        imprimirValor(i)
    menu()

def imprimeListaOrdenada():
    lista.sort()
    print("lista ordenada crescente")
    for i in lista:
        imprimirValor(i)
    menu()

def imprimeListaOrdenada2():
    lista.reverse()
    print("lista ordenada descresente")
    for i in lista:
        imprimirValor(i)
    menu()

def menu():
    print("*************************************")
    print("            Menu                     ")
    print("*************************************")
    print(" 1 - entre com os números")
    print(" 2 - Imprime lista dos valores")
    print(" 3 - Imprime a lista ordenada Crescente")
    print(" 4 - Imprime a lista ordenada Decrescente")
    print(" 0 - ZERO para encerrar o programa")
    print("*************************************")
    print()

    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):
        num = int(input("Entre com a quantidade de números: "))
        ent_num(num)
    elif(opcao == 2):
        imprimeLista()
    elif (opcao == 3):
        imprimeListaOrdenada()
    elif (opcao == 4):
        imprimeListaOrdenada2()
    elif (opcao == 0):
        print("saindo da agenda...")
        print("Agenda Finalizada")
    elif opcao <= 0 or opcao >=4:
        print("************************************************************")
        print("   OPÇÃO INVÁLIDA - POR FAVOR, DIGITE UM NÚMERO DE 0 A 4!")
        print("************************************************************")


lista = []
## inicio do programa
menu()