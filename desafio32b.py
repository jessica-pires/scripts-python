#calcular se o ano  atual é bissexto ou nao

from datetime import date
ano  = int(input('digite 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano atual {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto'.format(ano))