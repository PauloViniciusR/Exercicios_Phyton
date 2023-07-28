"""
    Faça um algoritimo que leia o salario e mostre o salario com uma porcentagem de aumento
"""

salario = float(input("Digite o seu sálario: R$"))
new_salario = salario + (salario * 15 / 100)

print("Você recebeu um aumento, será de R${:.2f}".format(new_salario))

