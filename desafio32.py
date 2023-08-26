#dizer se o ano é bissexto nao nao------
ano = int(input('digite o ano que quer analisar: '))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano não é BISSEXTO'.format(ano))
