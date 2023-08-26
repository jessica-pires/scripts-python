#programa que leia um numero inteiro e
#diga se le é  um Numero primo.
total = 0
num = int(input('digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        total = total + 1
        print('{}'.format(c), end=' ')
print('\nO numero {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('Ele é um numero primo.')
else:
    print('Ele nao é um numero primo.')