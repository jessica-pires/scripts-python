#programa que calcule o IMC de uma pessoa e dida se ela esta abaixo ou acima do seu peso ideal

peso = float(input('qual seu peso: '))
altura = float(input('qual sua altura: '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('IMC {:.1f} Você esta abaixo do seu peso ideal'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('Seu IMC é {:.1f} Você esta no peso ideal'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('Seu imc é {:.1f} Você esta com sobrepeso'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('Seu imc é {:.1f} Você esta com obesidade'.format(IMC))
else:
    print('Seu imc é {:.1f}. Obesidade morbida'.format(IMC))
