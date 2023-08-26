#programa que mostre quantas vezes aparece a letra A
#em que posicao aparece pela primeira e ultima vez

frase = str(input('diga uma frase: ')).upper().strip()
print('a letra a aparece {} vezes na frase.'.format(frase.count('A')))
print('a primeira letra A apareeu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posiçaõ {}'.format(format(frase.rfind('A')+1)))

#+1 para contagem comecar do 1, 2, 3, 4, 5,
#rfind == encontrar elemento da direita 'right find'

#print(frase.count('a'))



