"""Crie um programa que leia a quantidade de dinheiro 
    e quantos dolares pode comprar"""

real = float(input('Digite o valor: R$'))
dolar = real / 4.74

print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
