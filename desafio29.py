# leia a velocidade de um carro
#se ultrapassar 80km\h mostre uma
#msg dizendo que ele foi multado
#  multa custa $7 reais para cada km acima do limite

velocidade = float(input('qual a velocidade km\h: '))
multa  = (velocidade-80) * 7
if velocidade > 80 :
    print('MULTADO, voce foi multado em R${:.0f} reais '.format(multa))
else:
    print('Siga em frente, boa viagem')