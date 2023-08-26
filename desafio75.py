num = (int(input('digite um numero'))), (int(input('digite outro numero'))), (int(input('digite mais um numero'))), (int(input('digite o ultimo numero')))
print(f'Voce digitou {num}')

if 9 in num:
        print(f'O numero 9 apareceu {num.count(9)} vezes')
else:
        print('O numero 9 nao foi digitado')
if 3 in num:
    print(f'O numero 3 esta na posicao {num.index(3)+1}')
else:
    print('o numero 3 nao foi  digitado')
print('Os numeros pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
