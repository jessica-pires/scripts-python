#--------ler o salario de um funcionario e mostra seu novo
# salario com 15% de aumento

sal = float(input('qual seu salario:'))
nS = sal *1.15
print('o seu aumento é de {:.2f}'.format(nS))

#=========Outro forma de mostrar o calculo é:
print(' Seu salario de  {} com aumento de 15% é {:.2f}'.format(sal,sal*1.15))
