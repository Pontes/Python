import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************************")
    print("***  Escolha o seu jogo ***")
    print("*********************************************")

    print(" (1) Forca (2) Adivinhação ")

    jogo = int(input("Escolha um jogo: "))

    if(jogo ==1):
        print("Jogando Forca")
        forca.jogo()
    elif(jogo ==2):
        print("Jogando adivinhação")
        adivinhacao.jogo()

if(__name__ == "__main__"):
    escolhe_jogo()