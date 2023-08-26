# aumento de salario para 15% ate $1.250
#aumento de 10% acima desse valor
salario = float(input('qual seu salario:'))
if salario <= 1.250:
   aumento =  salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 /100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, aumento))
