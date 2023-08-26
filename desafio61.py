#progressao aritmetica
#programa que leia o primeiro termo e a razao de uma pa.
# no final mostre os 10 primeiros termos dessa progressao.
primeiro= int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont = cont +1
print('FIM')

