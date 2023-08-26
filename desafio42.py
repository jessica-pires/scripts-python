#programa que leia um triangulo acrescentando o recurso de
# mostrar que tipo de triangulo sera formado: EQ, ISÓ, ES
#Equilátero: quando todos os lados têm o mesmo comprimento.
#Isósceles: quando pelo menos dois lados têm o mesmo comprimento.
#Escaleno: quando todos os lados têm comprimentos diferentes.

lado1 = int(input('qual o primeiro segmento: '))
lado2 = int(input('qual o segundo segmento: '))
lado3 = int(input('qual o terceiro semento: '))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Este é um triangulo EQUILÁTERO')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Este é um triângulo ISÓSCELES')
else:
    print('Este é um triângulo, ESCALENO')