# programa que calcule a soma entre todos os numero
#impares que sao nultiplos de 'tres'
#e se encontram no intervalo de 1 ate 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont +1
        soma = soma + c
print(' a soma de todos {} numeros é {}'.format(cont, soma))


        