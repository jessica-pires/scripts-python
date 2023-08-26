#copie o codigo 61 e pergunte para o usuario se ele quer mostrar mais alguns termos
#. o programa encerra quando ele disser que quer mostrar 0 termos
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont +=1
    print('PAUSA')
    mais = int(input('quantos termos voce quer mostrar a mais: '))
print('progressao finalizada com {} termos mostrados'.format(total))