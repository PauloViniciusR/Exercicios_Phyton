"""Crie um conversor de moedas"""

real = float(input('Digite o valor: R$'))
dolar = real / 4.74
euro = real / 5.25

print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(real, euro))
