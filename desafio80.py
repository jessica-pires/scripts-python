lista = []
for c in range(1, 5):
    lista.append(int(input('Digite um valor: ')))
for i, c in enumerate(lista):
     print(f'na posicao {i+1} encontrei o valor {c}')

lista.sort()
print(f' Valores digitados: {lista} ')
