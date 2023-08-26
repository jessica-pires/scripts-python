numero = []
pegar = [[], []]
for cont in range(1, 7):
    numero = int(input(f'digite {cont}o. numero: '))
    if numero % 2 == 0:
             pegar[0].append(numero)
    else:
             pegar[1].append(numero)
print(f'Ao todo os numeros digitados foram {pegar}')
print(f'os numeros pares digitados sao {pegar[0]}')
print(f' os numeros impares digitados foram {pegar[1]}')