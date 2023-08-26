#programa que leia o nascimento de
# um atleta e mostre sua
# categoria de acorodo com a idade:
from datetime import date

nasci = int(input('qual sua idade: '))
ano_atual = date.today().year

idade = ano_atual - nasci
if idade <= 9:
    print('Mirim')
elif idade  >  9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')