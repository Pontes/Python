def mostrar(texto, contador):
    saida = open(texto, 'r')
    for x in saida:
        linha = saida.readline()
        print(linha.strip())

    print("----------------------------------------")
    print(f'Wally apareceu: {contador}')

def procurar(entrada, saida):
    arqEntrada = open(entrada, 'r')
    arqSaida = open(saida, 'w')
    contador= 0
    for x in arqEntrada:
        linha = arqEntrada.readline()
        if "Wally" in linha:
            contador += 1
        else:
            arqSaida.write(linha)
    arqEntrada.close()
    arqSaida.close()
    mostrar(saida, contador)
    return None


def main():
    proc = input('Digite o nome do arquivo de entrada: ')
    sai = input("Digite o nome do arquivo de saída: ")
    procurar(proc, sai)


main()