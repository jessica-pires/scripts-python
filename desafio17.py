# faça um programa que leia o comprimento do
# cateto oposto e do cateto adjacente de um triangulo retangulo.
# calcule e mostre o comprimento da hiptenusa

#forma tradicional sem importação
catetoO = float(input('cateto oposto: '))
catetoA = float(input('cateto adjacente: '))
hipoenusa = (catetoO ** 2 + catetoA **2) **(1/2)
print('A hiptenusa vai medir {:.2f}'.format(hipoenusa))

#forma atraves do import expecifico
from math import hypot
catetoO = float(input('cateto oposto: '))
catetoA = float(input('cateto adjacente: '))
hipotenusa = hypot(catetoO, catetoA)
print('a hipoenusa vai medir {:.2f}'.format(hipotenusa))




