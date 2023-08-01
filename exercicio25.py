"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
nome = str(input("Informe seu nome completo: "))
print("Seu nome tem Silva? {}".format('silva' in nome.lower()))
