"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.
"""
"""  
oposto = float(input("Comprimeto do cateto oposto: "))
adjascente = float(input("Comprimento do cateto adjascente: "))

hipotenusa = (oposto** 2 + adjascente ** 2) ** (1/2)

print("A hipotenusa mede {:.2f}".format(hipotenusa))

"""

#Com importação
import math
oposto = float(input("Comprimeto do cateto oposto: "))
adjascente = float(input("Comprimento do cateto adjascente: "))

hipotenusa = math.hypot(oposto, adjascente)

print("A hipotenusa mede {:.2f}".format(hipotenusa))

