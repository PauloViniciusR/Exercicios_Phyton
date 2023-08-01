"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = int(input('Informe seu salario: R$'))

if salario <= 1320:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print("O seu novo salário será de R$ {:.2f}".format(novo))
