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

primeiroNumero = input("Digite o primeiro número: ")
operacao = input("Digite a operação desejada (+,-, *, / ou //): ")
segundoNumero = input("Digite o segundo número: ")

formula = primeiroNumero + operacao + segundoNumero
resultado = eval(formula)
print(resultado)