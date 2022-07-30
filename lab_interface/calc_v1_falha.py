#!/usr/bin/env python
# coding: UTF-8
#
#  @package calc_v11.py
#
#  ./calc_v11.py
#
#  Simple calculator in terminal
#
#  @author André Saraiva
#  @since 15/02/2022

primeiroNumero = int(input("Digite o primeiro número: "))
operacao = int(input("Digite a operação desejada (+,-, *, / ou //): "))
segundoNumero = int(input("Digite o segundo número: "))

resultado = primeiroNumero + operacao + segundoNumero

print(resultado)
