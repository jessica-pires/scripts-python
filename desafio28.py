#comando onde o pc 'PENSE' um numero entre 0 a 5
#e peca para o usuario tentar descobrir
# qual foi o numero escolhido pelo pc

#=-=-=-=-=-JOGO DE ADVINHAÇÃO=-=-=-=-=-=-=-=-
from random import randint #importando numeros aleatorios
from time import sleep #importando tempo de processamento

numeroAleatorio = randint(0, 5) #faz o computador pensar

#print('Tente adivinhar: {}'.format(numeroAleatorio))
print('==-==-'*10)
jogador = str(input('Em que numero eu pensei: ')) #adivnhar numero
print('PROCESSANDO')
sleep(2)
print('==-==-'*10)
if jogador == numeroAleatorio:
    print('Parabens, usuario consegui me vencer!')
else:
    print('Ainda não, continue tentando,eu pensei {} e voce {}'.format(numeroAleatorio, jogador))
print('----fim-----')

