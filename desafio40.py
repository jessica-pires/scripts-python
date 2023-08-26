#programa que leia duas notas de um aluno e calcule sua media, mostrando uma
# mensagem no final, de acoros com a media

print('=-=-==-=-'*5)
nota1 = float(input('Sua primeira nota: '))
nota2 = float(input('Sua segunda nota: '))

media = (nota1 + nota2) / 2
if media < 5.0:
    print('Você foi REPROVADO')
elif media > 5.0 and media < 6.9:
    print('Você esta em RECUPERAÇÂO')
else:
    print('APROVADO')
