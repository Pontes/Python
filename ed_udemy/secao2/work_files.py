def exibir(arqx):
    arquivo = open(arqx,'r')
    for x in arquivo:
        print(x)

    arquivo.close()

def gravar(arqx, texto):
    arquivo = open(arqx,'a')
    arquivo.write(f'{texto}\n')
    arquivo.close()
    return f'{texto} gravado com sucesso!'

def buscar(arqx, texto):
    arquivo = open(arqx, 'r')
    conta = 0
    for x in arquivo:
        linha = arquivo.readline()
        if texto in linha:
            conta = 1
            print("*** Texto encontrado! ***")
            print(f'pesquisa sobre: {texto}')
            print(f'{linha}')
            print("*"*25)
            print("")
            break
    if conta == 0:
        print(f'*** Não foi encontrado o conteúdo sobre {texto} ***')
        print("")

    arquivo.close()

def menu():
    print("******** MENU PRINCIPAL *********")
    print("*** 1 - LER ARQUIVO       ***")
    print("*** 2 - GRAVAR ARQUIVO    ***")
    print("*** 3 - BUSCAR NO ARQUIVO ***")
    print("*********************************")
    print("")

def main():
    arquivo = 'agenda.txt'
    try:
        f = open(arquivo)
        f.close()
    except:
        f = open(arquivo,'w')
        f.close()

    while True:
        menu()
        op = int(input("Digite a opção desejada: "))
        if op ==1 :
            exibir(arquivo)
        elif op == 2 :
            texto = input("Digite o nome e telefone (nome - (00) 00000-0000: ")
            gravar(arquivo, texto)
        elif op == 3:
            texto = input("Digite o nome ou telefone: ")
            buscar(arquivo, texto)
        else:
            print("*** ATENÇÃO ***")
            print("Opção inválida!")
            print("***************")
            print("")

main()