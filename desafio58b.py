from random import randint
computador = randint(0, 10)
palpite = 0
jogador = int(input('qual seu palpite: '))
while jogador != computador:
    jogador = int(input('qual seu palpite: '))
    palpite += 1
    if jogador > computador:
        print('menos, tente novamente.')
    elif jogador < computador:
        print('mais..tente novamente')
print('parabens, voce acertou na  {}ª tentativas'.format(palpite))
