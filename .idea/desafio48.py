#programa que calcule a soma entre todos os
# numeros impares que sao multiplos por 3
# e se encontram no intervalo de 1 ate 500
soma = 0
cont = 0
for c in range(1, 500, 2 ):
    if c % 3 ==0:
        cont = cont +1
        soma = soma + c
print('A soma de todos os {} os valores é {}'.format(cont, soma))

