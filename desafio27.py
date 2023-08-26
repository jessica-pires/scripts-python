#programa que leia o nome completo
# de uma pessoa mostrnado o primeiro e ultimo nome

nome = input('Seu nome completo: ').strip()
primeiroNome = nome.split()
ultimoNome = nome.split()
print('seu primeiro nome é {}{}{}'.format('\033[0;31;47m', primeiroNome[0], '\033[m'))
print('Seu ultimo nome é {}{}{}'.format('\033[4;30;46m', ultimoNome[-1], '\033[m'))

