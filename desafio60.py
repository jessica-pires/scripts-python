#programa que mostre um valor e seu fatorial
numero = int(input('Digite um numero que mostro o seu fatorial: '))
recebe_numero = numero
fatorial = 1 # recebe 1 pois na multiplicacao comeca com 1
while recebe_numero > 1:
    print('{} '.format(recebe_numero), end='')
    print('x ' if recebe_numero > 1 else '=', end='')
    fatorial = fatorial * recebe_numero
    recebe_numero = recebe_numero -1
print('{}'.format(fatorial))
