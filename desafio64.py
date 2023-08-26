soma = 0
cont = 0
n = 0
n = int(input('digite um numero [999 pars parar]: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('digite um numero [999 pars parar]: '))
print('voce digitou {} numeros e a soma entre eles foi{}'.format(cont, soma))