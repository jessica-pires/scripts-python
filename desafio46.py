#contagem regressiva de 10 a 0 com estouro de fogods
from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print(emoji.emojize('\033[0;44mFeliz ano novo\033[m:fireworks:'))
print(emoji.emojize(':fireworks:' *5)) #fogos de artificio