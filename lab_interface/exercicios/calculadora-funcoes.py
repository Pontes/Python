def somar(x,y):
    return int(x) + int(y)

def subtrair(x,y):
    return int(x) - int(y)

def multiplicar(x,y):
    return int(x) * int(y)

def dividir(x,y):
    if y == 0:
        return 'Não é possivel divisão por zero!'
    else:
        return int(x) / int(y)

def impressao():
    print("*** Programa Calculadora ***")
    print("****************************")
    print("Digite Q para finalizar.")

def tratarDados(x):
    if 'q'== x or 'Q' == x:
        print('Finalizando...')
        exit()

def entrarDados():
    num1 = input("Digite o Primeiro Valor: ")
    tratarDados(num1)
    print("Digite o operador")
    print('(+) para somar')
    print('(-) para subtrair')
    print('(*) para multiplicar')
    print('(/) para dividir: ')
    operador = input('Qual operador: ')
    num2 = input("Digite o Segundo Valor: ")
    tratarDados(num2)
    lista = [num1, operador, num2]
    return lista

def main():
    impressao()
    while True:
        op = entrarDados()
        if op[1] == '+':
            x = somar(op[0],op[2])
        elif op[1] == '-':
            x = subtrair(op[0],op[2])
        elif op[1] == '*':
            x = multiplicar(op[0],op[2])
        elif op[1] == '/':
            x = dividir(op[0],op[2])

        print("Resultado: ", x)

main()
