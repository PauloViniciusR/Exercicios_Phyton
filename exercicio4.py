"""
    Criar um programa que leia e mostre o tipo primitivo e todas as informação
    possiveis sobre ela
    """
a = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(a))
print('Somente espaços: ', a.isspace())
print('é uma numero: ', a.isnumeric())
print('É alfabeto: ', a.isalpha())
print('É alfanumerico: ', a.isalnum())
print('Está maiusculo: ', a.isupper())
print('Está em minusculo: ', a.islower())
print('Está capitalizada: ', a.istitle())
