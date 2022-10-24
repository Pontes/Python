def lerValores():
    t = int(input('Digite o tempo de viagem em horas: '))
    v = int(input('Digite a velocidade média da viagem: '))
    return t,v

def calcularDistancia(t, v):
    d = t * v
    return d

def calcularQtdLitros(d):
    litrosUsados = d /12
    return litrosUsados

def resultado(t, v, d, l):
    print(f'Tempo de viagem: {t}')
    print(f'Velocidade média: {v}')
    print(f'Distancia percorrida: {d}')
    print(f'Quantidade de litros utilizados: {l}')


t,v = lerValores()
d = calcularDistancia(t,v)
l = calcularQtdLitros(d)
resultado(t,v,d,l)

