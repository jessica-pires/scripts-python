
pessoa =  homen = mulher =  0
pergunta = ' '

while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '#str(input('Qual seu sexo? [F/M]')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Qual seu sexo? [F/M]')).upper().strip()[0]

    if idade >= 18:
        pessoa = pessoa + 1
    if sexo == 'M':
        homen = homen + 1
    if idade <= 20 and sexo == 'F':
        mulher = mulher + 1




    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? S/N')).upper().strip()[0]
    if pergunta == 'N':
        break



print(f'A) tem {pessoa} pessoas maiores de 18 anos')
print(f'B) Ao todo temos {homen} homens cadastrados')
print(f'C) E temos {mulher} mulheres com menos de 20 anos')
