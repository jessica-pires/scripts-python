lista = []
valor = []

par = []
ímpar = []
while True:
    lista.append(int(input('digite um valor: ')))
    pergunta = str(input('quer continuar? [S/N]: '))
    if pergunta in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        ímpar.append(v)

print(f' os numeros digitados foram {lista}')
print(f' Numeros pares foram {par}')
print(f' numeros ímpares foram {ímpar}')
