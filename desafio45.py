# programa que faça o pc jogar pedra papel tesoura
from random import randint
numero_sorteado = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('Suas Opções')
print('[0] pedra')
print('[1]papel')
print('[2]tesoura')
jogador = int(input('Qual a sua jogada: '))
print('-='*11)
print('O computador jogou {}'.format(numero_sorteado[computador]))
print('O jogador jogou {}'.format(numero_sorteado[jogador]))
print('-='*11)

if computador ==0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador VENCE')
    elif jogador == 2:
        print('computador VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: # tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')



