#função sem parametro e sem retorno

def mensagem():
    print('Estudar função')

#funão com passagem de parametro

def mensagem2(texto):
    print('Mensagem:', texto)

def soma(a,b):
    print(a+b)

#função com passagem de parametro e retorno
def somatorio(x,y):
    return x+y

def calcula_energia_potencial_gravitacional(m , h, g = 10):
    '''
    Calcula a energia potencial gravitacional
    Argumentos:
    :m: massa, entrada como uma variavel float
    :h: altura, entrada como uma variável float
    Argumento opcional:
    :g: aceleração gravitacional, com valor default de 10
    '''
    e = g * m * h
    return e


mensagem()
mensagem2('você está aprendendo python')
soma(10,25)
print(somatorio(20,5))
help(calcula_energia_potencial_gravitacional)
print('Calcul gravitacional: ',calcula_energia_potencial_gravitacional(30,12))
print('Calcul gravitacional: ',calcula_energia_potencial_gravitacional(30,12,9.8))
print('fim das funções')