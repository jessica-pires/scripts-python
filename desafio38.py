#programa que leia dois mumeros inteiros e compare-os, mostrando a tela uma mensagem:
# -O primeira valor é maior
# -O segundo o valor é maior
# -Não existe valor maior, os dois são iguais

p = int(input('digite o primeiro número: '))
s = int(input('digite o segundo número: '))

if p > s :
    print('O primeiro  valor {} é maior que {}!'.format(p, s))
elif s > p :
    print('{} é maior que {}!'.format(s, p))
elif p == s and s == p :
    print('Não existe valor maior, os dois são iguais')