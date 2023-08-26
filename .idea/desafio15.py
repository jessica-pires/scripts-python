#----------escrever um programa que pergunte a quantidade
# de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado.
#calcule  o preço a pegar, sabendo que o  carro
#custa $60 por dia e 0,15 po km rodado

dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos kilometros percorridos?: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))