lista1 = []

while True:
    lista1.append(int(input('Digite um valor: ')))
    pergunta = str(input('deseja continuar [S/N]: ')).upper().strip()[0]
    if pergunta in 'N':
        break
numeros_pares = [numero for numero in lista1 if numero % 2 == 0]
nueros_impares = [numero for numero in lista1 if numero % 2 != 0]


print(f'A lista completa é {lista1}')
print(f' Os numeros pares são {numeros_pares}')
print(f'Os numeros impares são {nueros_impares}')
