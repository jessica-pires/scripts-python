valor = []

while True:
    numero = int(input('Digite um numero:' ))


    if numero not in valor:     #se numero nao estiver em valor # ....adicione a lista...usando .append()
        valor.append(numero)
        print('Valor adicionado com sucesso')
    else:
        print('numero repetido !Nao adicionado')
    pergunta = str(input('deseja continuar? [S/N]:')).upper().strip()[0]
    if pergunta in 'Nn':
        break

valor.sort()
print(f'lista de numeros {valor}')