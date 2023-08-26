#opcao usando max e min

lista = []
pegar_lista = []

while True:
    lista.append(str(input('qual seu nome: ')))
    lista.append(float(input('Qual seu peso: ')))
    pegar_lista.append(lista[:])
    lista.clear()


    pergunta = str(input('Quer cotinuar? [S/N]: ')).upper().strip()[0]
    if pergunta in 'N':
             break
print(f'Ao todo foram {len(pegar_lista)} pessoas cadastradas')
print(f'a pessoas mais pesada tem {} kilos')
