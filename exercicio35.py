"""Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.
"""
r1 = float(input('Informe o primeiro lado: '))
r2 = float(input('Informe o segundo lado: '))
r3 = float(input('Informe o terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("O segmento acima podem formar um triangulo")
else:
    print("O segmento acima não podem formar um triangulo")
