#pergunte a distancia de uma viagem em km
#Calcule o preço da passagem , cobrando 0,50 por km
#para viagem ate 20km. e 0.45 acima de 200 km

distancia = float(input('Qual a distancia do km: '))
print('voce esta prestes a comecar ua vigem de {} km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('voce vai pagar {}'.format(preco))
else:
    preco = distancia *0.45
    print('é o preco da sua passagem será de R${}'.format(preco))