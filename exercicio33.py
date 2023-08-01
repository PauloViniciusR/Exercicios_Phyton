"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("O menor valor foi: {}".format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior valor foi: {}".format(maior))

