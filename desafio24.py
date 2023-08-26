#programa que leia o nome de uma cidade e diga se ela
# começa ou não com a letra SANTO

cidade = str(input('qual sua cidade? ')).strip()
print(cidade[0:5].upper() == 'SANTO')
