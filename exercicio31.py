""" Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

distancia = int(input("Informe a distancia da viagem: "))
print("oce esta prestes a começar uma viagem de {}Km.".format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O valor da sua viagem é de {:.2f}".format(preco))

