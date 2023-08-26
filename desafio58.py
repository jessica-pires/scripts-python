#comando onde o pc 'PENSE' um numero entre 0 a 5
#e peca para o usuario tentar descobrir
# qual foi o numero escolhido pelo pc

#=-=-=-=-=-JOGO DE ADVINHAÇÃO=-=-=-=-=-=-=-=-
from random import randint #importando numeros aleatorios
from time import sleep #importando tempo de processamento

numeroAleatorio = randint(0, 10) #faz o computador pensar
print('Sou seu computador...')
print('acabei de pensar em um numero entre 1 e 10')
print('Sera que vpce conseue advinhar qual foi?')

from random import randint
numeroAleatorio = randint(0, 10)

acertou = False
palpite = 0
while not acertou:
        jogador = int(input('qual sei palpite: '))
        palpite = palpite + 1
        if jogador == numeroAleatorio:
            acertou = True
        else:
            if jogador < numeroAleatorio:
                print('Mais ....tente novamente.')
            elif jogador > numeroAleatorio:
                print('menos...Tente novamente.')
print('voce acertou com {} tentativas'.format(palpite))




       


