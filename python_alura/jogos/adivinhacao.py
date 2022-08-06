import random

def jogo():

    print("*********************************************")
    print("Bem vindo no jogo de adivinhação")
    print("*********************************************")

    numerosecreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)Fácil  (2) Médio  (3) Difícil")

    nivel =  int(input("Defina a nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas +1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numerosecreto
        maior   = chute > numerosecreto
        menor   = chute < numerosecreto

        if(acertou):
            print("Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("você errou!! o seu chute foi maior do que o numero secreto")
            elif(menor):
                print("você errou!! o seu chute foi menor do que o numero secreto")

            pontos_perdidos = abs(numerosecreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo()
