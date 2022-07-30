#Funções: entraValores, somaValores, subtraiValores, multiplicaValores, divideValores e imprimeResultado
#Deivid Hugo dos Santos Ramos - 202022731

def entraValores():
    numero = input('Insira um número: ')
    return numero

def somaValores(primeiro, segundo):
    return eval(primeiro) + eval(segundo)

def subtraiValores(primeiro, segundo):
    return eval(primeiro) - eval(segundo)

def multiplicaValores(primeiro, segundo):
    return eval(primeiro) * eval(segundo)

def divideValores(primeiro, segundo):
    return eval(primeiro) / eval(segundo)

def imprimeResultado(solucao): #Apresentar na saída padrão (vídeo) o resultado.
    print(f'O resultado é : {solucao}')

def encerar(verifica): #Ter uma ou mais funções para entrada dos números ou se a letra “q” for pressionada, encerrar a aplicação;
    if ('Q' in verifica.upper()):
        return False

def escolha():
    while True:
        x = input('Insira a operacao: ')
        if ( x == '+' or x == '-' or x == '*' or x == '/'):
            return x
        else:
            print('Você não insirou nenhum operador ( +, -, *, /), Try Again!')
            continue

def Caculadora(): #Ter uma função para escolha das operações citadas de forma que se o usuário pressionar + uma função soma irá efetuar a operação com os dois números;
    while True:
        try:
            print('==== Calculadora ====')
            one = entraValores()
            if ( encerar(one) == False): 
                print('CALCULO ENCERRADO!')
                break
            operador = escolha()
            two = entraValores()
            if ( operador == '+'):
                conta = somaValores(one,two)
            elif ( operador == '-'):
                conta = subtraiValores(one,two)
            elif ( operador == '*'):
                conta = multiplicaValores(one,two)
            elif ( operador == '/' ):
                conta = divideValores(one,two)
            imprimeResultado(conta)
            break
        except:
            print('Há algo de errado na sua operação, Try Again!!!')
            continue

Caculadora()