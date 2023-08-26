#programa que leia o ano de nascimento de 7 pessoas no final,
# mostre quantas pessoas ainda
#nao atingiram a maioridade e quem ja atingiu.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for nasc in range(1, 7):
    nasc = int(input('qual ano a pessoa nasceu:'))
    idade = atual - nasc
    if idade >= 21:
        maior = maior +1
    else:
         menor = menor +1
print('ao todo tiveram {} maiores'.format(maior))
print('ao todo tiveram {} menores'.format(menor))
