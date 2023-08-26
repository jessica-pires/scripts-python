#programa onde um professor escolhe dentro de 4 alunos
# 1 para apagar o quadro
#------sorteando um intem da lista------------#
#usando a biblioteca randow

from random import choice # choice significa escolha
primeiroA = str(input('primeiro aluno: '))
segundoA = str(input('Segundo aluno : '))
terceiroA = str(input('Terceiro aluno: '))
quartoA = str(input('Quarto aluno: '))
LISTA = [primeiroA, segundoA, terceiroA, quartoA]
escolhido = choice(LISTA)
print('O aluno escolhido foi {}'.format(escolhido))
