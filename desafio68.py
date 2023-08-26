from random import randint
vitoria = 0
print('=-'*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*12)
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    resultado = computador + jogador
    escolha = ' '
    while escolha not in 'PIÍ':
        escolha = str(input('Escolha PAR OU ÍMPAR: ')).upper().strip()[0]
    print(f' Você escolheu {jogador} e o computador {computador}. Total de  {resultado}', end=' ')
    if resultado % 2 == 0:
        print('DEU PAR')
    else:
        print('DEU IMPAR')
    if escolha == 'P':
        if resultado % 2 == 0:
            print('Voce venceu...')
            vitoria = vitoria + 1
        else:
            print('Você perdeu...')
            break
    elif escolha == 'I':
        if resultado % 2 != 0:
            print('voce venceu ')
            vitoria = vitoria + 1
        else:
            print('voce perdeu')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER!.... Você venceu {vitoria}x')





