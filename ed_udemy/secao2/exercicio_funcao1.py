def lerTemp():
    temp = float(input('Digite a temperatura em Cº: '))
    return temp

def calculaTemp(x):
    c = x
    f = (9 * c + 160) / 5
    return f

def mostrarTemp(f):
    print(f'A Temperatura em Fahrenheit é de: {f}')


x = lerTemp()
tempF = calculaTemp(x)
mostrarTemp(tempF)

