#Faca um programa que mostre a tabuada de varios numeros,
#o programa sera interronpido quando o numero for negativo
resultado = c = 0

while True:
    numero = int(input('qual a tabuada:'))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {resultado}')
    c = c + 1
    resultado = numero * c
    print(f'{numero} x {c} = {resultado}')
print('Programa encerrado volte sempre')



