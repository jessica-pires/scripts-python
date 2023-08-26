#programa que leia 3 numeros
#mostre qual é o maior
#mostre qual o menor

primeiroN = int(input('qual o primeiro numero:  '))
segundaN = int(input('qual o segundo numero: '))
terceiroN = int(input('qual o terceiro numero: '))
maior = primeiroN
if primeiroN > segundaN and primeiroN > terceiroN:
     maior = primeiroN

if segundaN > primeiroN and segundaN > terceiroN:
    maior = segundaN

if terceiroN > primeiroN and terceiroN > segundaN:
    maior = terceiroN

if primeiroN < segundaN and primeiroN < terceiroN:
    menor = primeiroN
if segundaN < primeiroN and segundaN < terceiroN:
    menor = segundaN
if terceiroN < primeiroN and terceiroN < segundaN:
    menor = terceiroN

print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))


