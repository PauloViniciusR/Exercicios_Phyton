"""
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import trunc

number = float(input("Insira um numero: "))
print("Valor digitado foi {} e sua porção inteira é {}".format(number, trunc(number)))
