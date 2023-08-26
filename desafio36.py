#programa para aprovar um emprestimo para um imovel
#a prestacao nao pode exeder 30% do salario

valorCasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salario R$ '))
anos = int(input('Quantos anos pretende pagar'))

#calculo da prestacao mensal

meses = anos * 12
prestacao = valorCasa / meses

#verificacao se a prestacao exede 30% do salario

limite_prestacao = salario * 0.3

if prestacao > limite_prestacao:
    print('Emprestimo negado. O valor da prestação exede 30% do seu salario')
else:
    print('Emprestimo aprovado! o valor da prestação mensal sera de {:.2f}'.format(prestacao))