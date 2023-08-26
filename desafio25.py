# programa que leia o nome de uma
# pessoa e diga se tem silva no nome

nome = str(input('qual seu nome: ')).strip()
print('seu nome tem Silva? {} '.format('silva' in nome.lower()))