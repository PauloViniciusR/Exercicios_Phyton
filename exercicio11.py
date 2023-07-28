"""
Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta 
necessária para pinta-la, sabendo que cada litro de tinta , pinta uma área
"""

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura
print("Sua parede tem a dimensão de {} x {} e sua área é de {}m2".format(largura, altura, area))

tinta = area / 2
print("Para pintar essa parede voce precisará de {}l de tinta". format(area))

