#programa que leia o ano de nsacimento e informe
# de acorod com sua idade: -Se ele vai se alista
# ao serviço militar
# -Se é hora de se alistar -Se ja passou do tempo do alistamento
from datetime import date
nasci = int(input('qual sua data de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - nasci

if idade == 18:

    print('Você tem {}. Esta na hora de se alistar'.format(idade))
elif idade < 18:
    anos_faltantes = 18 - idade

    print('Você  tem {} anos e faltam {} anos. Ainda vai se alistar ao serviço militar'.format(idade, anos_faltantes))
else:
    anos_passados = idade - 18
    print('Você tem {} e ja passou {} do tempo do alistamento'.format(idade, anos_passados))