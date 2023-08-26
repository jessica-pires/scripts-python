# estagistica de produtos
#1- total da compra
#2- produtos maiores de $1000
#3- produto mais barato
print('*******************')
print('LOJA SUPER BARATÃ0 ')
print('*******************')

total = totmil = menor_preco= cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco: float = float(input('Preço: R$'))
    cont = cont + 1
    total += preco
    #produto maior que mil
    if preco > 1000:
        totmil += 1
    #produto mais barato
    if cont == 1:
        menor_preco = preco
        barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            barato = produto

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if pergunta == 'N':
        break
print('----------FIM DO PROGRAMA-----------')
print(f'O total da compra foi {total}')
print(f'Temos {totmil:.2f} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {barato} que custou R${menor_preco:.2F}')