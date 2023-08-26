times = 'bota fogo', 'flamengo', 'palmeiras', 'gremio', "fluminense", 'bragantino', 'athletico-pr', 'sao paulo',
'cuiaba', 'cruzeiro', 'fortaleza', 'internacional','atletico-mg',
'corinthias', 'santos', 'goias', 'bahia', 'curutiba', 'america-mg','vasco da gama', 'imbituba'

print(f'Os cinco primeiros são: {times[0:5]}')
print('-------------------------------------')
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('-----------------------------------------')
print(f'Ordem alfabética dos times: {sorted(times)}')
print('--------------------------------------------')

print(f'O time do flamengo esta na  {times.index("flamengo")+1} posição')
print('-------------------------------------------------')
if times.count('chapecoense'):
    print(f'O time da chapecoense esta na {times.index("chapecoense")} posicao')
else:
    print(' a chapecoense nao esta na lista')
print('-------------------------------------------------------------------------------')

n = str(input('qual seu time? : '))
if n in times:
    print(f'Seu time {n} esta na {times.index(n)+1} posição ')
else:
    print('Seu time nao esta na lista do brasileirão')

print('obrigado')






