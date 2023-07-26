"""Desenvola um programa que leia as duas notas de um aluno, calcule
    e mostre a sua média"""

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média do aluno é de {:.1f}'.format(m))
