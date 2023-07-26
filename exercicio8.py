"""Escreva um programa que leia o valor em metro e exiba
    convertido em centimetros e milimetros"""

medida = float(input('Uma distancia: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000


print('A medida de {}m corresponde a: \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, dm, cm, mm))
print('A medida de {}m corresponde a: \n{:.1f}dam \n{:.2f}hm \n{:.3f}km'.format(medida, dam, hm, km))
