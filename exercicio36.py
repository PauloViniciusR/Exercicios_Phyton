"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Valor da casa: R$ '))
salario = float(input('Valor da casa: R$ '))
anos = int(input('Valor da casa: R$ '))

prestacao = casa / (anos * 12)

print("Para comprar essa casa de R${}, a prestação será de R${}".format())
