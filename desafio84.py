lista = []
pegar_lista = []

peso_pesado = peso_leve = 0
while True:
    lista.append(str(input('Seu nome: ')))
    lista.append(float(input('seu peso: ')))
    if lista[1] == 0:
        peso_pesado = peso_leve = lista[1]
    else:
        if lista[1] >peso_pesado:
            peso_pesado = lista[1]
        if lista[1] < peso_leve:
            peso_leve = lista[1]

    pegar_lista.append(lista[:])
    lista.clear()



    pergunta = str(input('Deseja continar? [S/N]: ')).upper().strip()[0]
    if pergunta in 'N':
        break
print(f'foram cadastradas {len(pegar_lista)} pessoas')
print(f'a pessoa mais pesada foi {peso_pesado}')
print(f' A pessoa mais leve de foi {peso_leve}')
