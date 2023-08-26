#elabore um programa que calcule o valor  ser pago
#por um produto considerando a condicao de pagamento
forma_pagamento = str(input('qual a forma de pagamento: '))
Valor_produto = float(input('qual valor do produto: '))
desconto = Valor_produto * 0.10
if forma_pagamento == 'avista':
    print('seu desconto foi de {:.0f} reais'.format(desconto))
elif forma_pagamento == 'cartao':
    desconto = Valor_produto * 0.05
    print('seu desconto foi de {:.2f} reais'.format(desconto))
elif forma_pagamento == '2x no cartao':
    print('Em 2x você não ganha desconto')
elif forma_pagamento == '3x no cartao':
    juros = Valor_produto * 0.20
    print('voce vai pagar {:.0f} reais de juros'.format(juros))

