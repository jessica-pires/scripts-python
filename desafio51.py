#programa que leia o primeiro termo e a razao de uma pa.
# no final mostre os 10 primeiros termos dessa progressao.


primeiro_termo = int(input('Primeiro termo: '))
razao= int(input('DE quanto em quanto:  '))
decimo = primeiro_termo + (10 -1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
      print(c, end=' -> ')
print('acabou')
