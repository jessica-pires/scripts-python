#Sorteando uma ordem na lista
from random import shuffle
n1 = str(input('primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('terceiro Aluno: '))
n4 = str(input('quaro Aluno : '))
lista =[n1, n2, n3, n4]
shuffle(lista)        #shuffle significa embaralhar
print('A ordem de apresentaçao será:')
print(lista)