"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

num = int(input("Informe um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
n = str(num)
print("Analisando o número {}".format(num))
print("Unidade: {}".format(u))
print("Unidade: {}".format(d))
print("Unidade: {}".format(c))
print("Unidade: {}".format(m))

