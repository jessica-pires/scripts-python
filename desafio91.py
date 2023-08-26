from random import randint
from datetime import time
c =0
jogogadores = {'jogador1': randint(1, 6),
                'jogador2': randint(1, 6),
                'jogador3': randint(1, 6),
                'jogador4': randint(1, 6)}

for k, v in jogogadores.items():
    print(f'O {k} tirou  {v}')
print()
print("-----RANKING DOS JOGADORES------")
print()

ganhadores = dict(sorted(jogogadores.items(), key=lambda item: item[1], reverse=(True)))
for k, v in ganhadores.items():
    print(f'Em {c+1}o. lugar {k} : {v}')
    c = c + 1