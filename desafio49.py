#refazer desafio 09 mostrando tabuada de um numero que o usuario
# escolher ultilizando for

numero = int(input('Qual a tabuada: '))
for c in range(1, 11):
        resultado = numero * c
        print('{} x {} = {}'.format(numero, c, resultado))
