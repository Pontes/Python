import random

def imprime_boasvindas():
    print("*********************************************")
    print("***  Bem vindo no jogo de forca ***")
    print("*********************************************")

def carrega_arq_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()
    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].upper()
    return palavra_secreta

def inicilizar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def entrada_dados():
    chute = input("Digite um letra: ")
    return chute.strip().upper()

def chute_certo(palavras, chute, letras_certas):
    index = 0
    for letra in palavras:
        if chute == letra:
            letras_certas[index] = letra
        index += 1

def imprime_msg_vencedor(palavra):
    print("****************************************************")
    print("***                Você Venceu!!                 ***")
    print("****************************************************")
    print("você acertou a palavra! {}".format(palavra.upper()))

def imprime_msg_perdedor():
    print("***************************************************")
    print("***                Você Perdeu!!                ***")
    print("***************************************************")

def imprime_msg_chute_erro(erros, palavra, tentativas):
    letrasFaltando = "_"not in palavra
    resta = tentativas - erros
    print("**************************************************************")
    print("***                   VOCÊ ERROU!!!!                       ***")
    print(f'Você já errou {erros} letras, falta apenas {resta} tentativas')
    print("**************************************************************")

def jogo():
    imprime_boasvindas()
    palavra_secreta = carrega_arq_palavra()
    letras_acertadas = inicilizar_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = len(palavra_secreta)

    print(letras_acertadas)
    ## enquanto não enforcou e não acertou
    while not enforcou and not acertou:

        chute = entrada_dados()

        if chute in palavra_secreta:
            chute_certo(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            imprime_msg_chute_erro(erros, palavra_secreta, tentativas)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_msg_vencedor(palavra_secreta)
    else:
        imprime_msg_perdedor()

if (__name__ == "__main__"):
    jogo()