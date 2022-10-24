def computador_escolhe_jogada(n, m):
    if n == 1:
        jogada = n - 1
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", m, " peças")

    return int(jogada)


def usuario_escolhe_jogada(n, m):
    i = 0
    while i == 0:

        jogada = input("Quantas peças você vai tirar? ")

        if jogada.isdigit():

            if int(jogada) > m or int(jogada) == 0:
                print("Oops! Jogada inválida! Tente de novo.")
                print("")
            else:
                n -= int(jogada)
                if int(jogada) > 1:
                    print("Você tirou ", int(jogada), " peças")
                else:
                    print("Você tirou uma peça.")

                i = 1

        else:
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
    return int(n)


def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    print("")

    if n % (m + 1) == 0:
        print("Computador começa!")
        print("")
        gameInicial = 1
    else:
        print("Você começa!")
        print("")

        gameInicial = 2

    i = gameInicial

    while n > 0:

        if i == 1:
            n = computador_escolhe_jogada(n, m)
            i = 2
        else:
            n = usuario_escolhe_jogada(n, m)
            i = 1

        if n > 1:
            print("Agora restam ", n, "peças no tabuleiro.")
            print("")
        else:
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro")
                print("")
            else:
                if i == 2:
                    print("Fim de jogo! O computador ganhou!")
                    print("")
                else:
                    print("Fim de jogo! Você ganhou!")
                    print("")
    return i


def campeonato():
    i = 0
    computador = 0
    jogador = 0
    while i < 3:
        resultado = partida()
        if resultado == 2:
            computador += 1
        else:
            jogador += 1

        i += 1

    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você", jogador, "X", computador, "Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato "))

    if opcao == 1:
        partida()
    else:
        if opcao == 2:
            campeonato()


main()












