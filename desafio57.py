#programa que leia o sexo de uma pessoa mas so aceite os valores M/F
# caso esteje errado peça a digitaçaõ novamente ate ter um valor correto
sexo = str(input('informe seu sexo:F/M: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Digite  seu sexo novamente: ')).upper()
print('sexo {} registrado com sucesso '.format(sexo))

