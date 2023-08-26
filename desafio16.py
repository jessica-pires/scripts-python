# crie um programa que leia um numero real e
# mostre na tela a sua posiçaõ inteira
from math import trunc
num = float(input('digite um numero: '))
r = trunc(num)
print('a porção inteira de {} é {}'.format(num, trunc(r)))

#ou de outra maneira sem usar o import match
print('a porcao inteira de {} é {}'.format(num, int(num)))
