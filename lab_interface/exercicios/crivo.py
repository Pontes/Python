def imprimePrimos(n, p):
    print(f'Os numeros primos de 2 até {n}' )
    #numFinal = n+1
    print(p);
    """
    for x in range(2,numFinal):
        if x in p:
            print(x)
    """
    return

def crivo(n):
    conjCrivo = set()
    resultado = set()
    conjVazio = set()
    z = 2

    for x in range(2, n+1):
        conjCrivo.add(x)

    while conjCrivo != conjVazio:
        while not (z in conjCrivo):
            z += 1

        resultado.add(z)
        secundaria = z

        while secundaria <= n:
            conjCrivo.discard(secundaria)
            secundaria += z

    return resultado

def main():
    numero = int(input('digite um valor para os números primos: '))
    primos = crivo(numero)
    imprimePrimos(numero, primos)

main()

