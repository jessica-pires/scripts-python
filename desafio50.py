#programa que leia seis numero inteiros
#e mostre a soma apenas daqueles que forem pares
#se for impar desconsiderar
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite o {} numero: '.format(c)))
    if c % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voce informou  {} números PARES e a soma foi {}'.format(cont, soma))
