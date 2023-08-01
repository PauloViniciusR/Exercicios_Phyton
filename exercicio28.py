"""
 Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário 
 tentar descobrir qual foi o número escolhido pelo computador. 
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
computador = randint(0, 5)
print("Pensei no número 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei: "))
print('Processando...')
sleep(3)

if jogador == computador:
    print("Parabéns, voce me venceu!!")
else:
    print("Ganhei, eu pensei no numero {} e não no {} tente novamente.".format(computador, jogador))

