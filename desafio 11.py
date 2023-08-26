#desafio que leia a largura e a altura de uma parede em metros
#calcule sua area
#e a quantidade de tinta necessaria para pinta-lá
#cada litro de tinta pinta uma area de 2m quadrados

l = float(input('qual a largura da parede: '))
a = float(input('qual a altura: '))

m2 = a * l
t = (a*l)/2
print('sua area é de {:.1f}'.format(m2))
print('voce vai precisar de {} litros  de tinta'.format(t))
