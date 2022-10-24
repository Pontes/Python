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


print("Calculadora de Fatorial - N! = N(N-1)*(N-2)*...*2*1")
print("===================================================")

numero = int(input("Digite um valor positivo: "))

if (numero < 0):
    print("Número negativo!!! Execução encerrada.")
else:
    fatorial = 1
    i = 1
    while (i <= numero):
        fatorial = fatorial * i
        i = i + 1
    print("O fatorial de %d = %d" %(numero,fatorial))
