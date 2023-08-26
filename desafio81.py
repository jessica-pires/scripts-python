lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('deseja continuar: ')).upper().strip()[0]
    if pergunta in 'N':
        break
print(f'a quantidade de numeros digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'Os valores em orem decrescente sao{lista}')
if 5 in lista:
    print(f'O valor  5 faz parte da lista, e esta na posiçao {lista.index(5)}')
else:
    print('numero 5 não esta na lista')