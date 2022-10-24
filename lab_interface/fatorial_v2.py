#!/usr/bin/env python
# coding: UTF-8
#
#  @package fat.py
#
#  ./fat.py
#
#  Calculadora de Fatorial
#
#  @author André Saraiva
#  @since 20/02/2022

def entraValor():
    numero = int(input("Digite um valor positivo: "))
    if (numero < 0):
        print("O número %d é negativo!!!" %(numero))
        numero = entraValor()
    return numero

def fatorial(numero):
    fatorial = 1
    i = 1
    while (i <= numero):
        fatorial = fatorial * i
        i = i + 1
    return fatorial

def main():
    resultado = fatorial(entraValor())
    print("O fatorial é %d" %(resultado))
    
main()
