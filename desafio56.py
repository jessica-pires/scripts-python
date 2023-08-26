#programa que leia nome idade e sexo de 4 pessoas
#no final mostre: quall a media de idade do grupo
#qual o nome do homen mais velho
#quantas mulheres tem menos de 20 anos
soma_idade = 0
mediaIdade = 0
maioridadehomen = 0
nomevelho =''
totmulher20 = 0

for p in range(1, 5):
    print('------------------------')
    print('--------{}ª Pessoa------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [S/N]: ')).strip()
    soma_idade = soma_idade + idade

    #NOME E IDADE DO HOMEN MAIS VELHO
    if p == 1 and sexo in 'Mn':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 =totmulher20 + 1
mediaIdade = soma_idade /4
print('A media de idade do grupo é {} anos'.format(mediaIdade))
print('O homen mais velho tem {} e se chama {}'.format(mediaIdade, nomevelho))
print('Ao todo sâo {} mulheres com menos de 20 anos'.format(totmulher20))