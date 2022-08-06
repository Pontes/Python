def jogo():
    print("*********************************************")
    print("***  Bem vindo no jogo de forca ***")
    print("*********************************************")

    palavra_secreta = "pontes".upper()
    quantidaLetras = len(palavra_secreta)
    erros = quantidaLetras + 3
    tentativas = resto = 0

    letraEscondidas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    print("A palavra secreta tem {} letras".format(quantidaLetras))
    ##print(letras_acertadas)
    print(f'Letras:  {letraEscondidas}')

    # enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input("Digite um letra: ")
        chute = chute.strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letraEscondidas[index] = letra
                index = index + 1
        else:
            tentativas = tentativas + 1
            resto = erros - tentativas


        letrasFaltando = str(letraEscondidas.count('_'))
        print(letraEscondidas)

        if(int(letrasFaltando)  == 0):
            acertou = True
            print("você acertou a palavra! {}".format(palavra_secreta.upper()))
        elif erros == tentativas :
            enforcou = True
            print("Você Enforcou")
        else:
            print("Ainda faltam acertar {} letras".format(letrasFaltando))
            print(f'Você já errou {tentativas} letras, falta apenas {resto}')



    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo()

