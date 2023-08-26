# dizer se o numero é ipa ou par
numero = int(input('me diga um numero qualquer: '))
if numero % 2 == 0 : #todo numero com resto de divisao por 2 em 0 é um numero par
    print('o numero {} é par'.format(numero))
else:
    print('o numero {} é impar'.format(numero))
