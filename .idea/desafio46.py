#programa que mostre uma contagem regressiva de 10 a 1
import emoji
from time import sleep
print('=-'*10)
print('\033[4;0;45mCONTAGEM REGRESSIVA\33[m')
print('-='*10)
for contagem in range(10 , -1, -1):
     print(contagem)
     sleep(0.5)
print(emoji.emojize('Vamos celebrar :fireworks:'))



