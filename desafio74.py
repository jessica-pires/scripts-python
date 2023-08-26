from random import randint
numero = (randint(1, 5), randint(1, 5), randint(1, 5),
    randint(1, 5), randint(1, 5))
print('Os numeros sortiados foram: ')
for n in numero:
    print(n, end=' ')
print(f'\nE o maior valor sorteado foi {max(numero)}')
print(f'E o menor valor sorteado foi {min(numero)}')



