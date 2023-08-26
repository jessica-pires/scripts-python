numero = 'zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    digite = int(input('Digite um numero entre 0 e 20: '))
    if digite > 20 or digite < 0:
        digite = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Voce digitou {numero[digite]}')
    pergunta = str(input('quer continuar: [S/N]: ')).upper().strip()[0]
    if pergunta =='N':
        break
    else:
        continue
print('obrigado')


