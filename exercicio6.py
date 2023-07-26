""" Crie um algotitimo que leia o numero e mostre o seu dobro, triplo e raiz quadrada"""

n = int(input('Digite um número: '))
d = n * 2 
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {} \nO triplo de {} vale {} \nA raiz quadrada de {} vale {:.3f}'.format(n, d, n, t, n, r))

