#crie um programa que lei o nome de completo de uma pessoa
#e mostre
#o nome com todas as letras maiusculas
#todas as letras minusculas
#quantas letras tem ao todo( sem considerar os espaços)
#quantas letras tem o primeiro nome

nome = str(input('Seu nome completo: ')).strip()
print(nome)
print('seu nome em maiúsculas é {}'.format(nome.upper()))
print('seu nome em ninúculas é {}'.format(nome.lower()))
print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

#duas opcoes para desafio dessa questao
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#ou
primeiroNome = nome.split()
print('seu pimeiro nome é {} e tem {} letras'.format(primeiroNome[0], len(primeiroNome[0])))