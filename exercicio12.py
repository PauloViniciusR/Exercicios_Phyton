"""
    Faça um algoritimo que leia o preço e aplique uma porcentagem de desconto
"""

valor = float(input("Insira o valor do produto: R$"))
desconto = valor - (valor * 50 / 100)

print("O valor do produto com desconto é R${}".format(desconto))
