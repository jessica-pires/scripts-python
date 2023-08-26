#programa que cria um menu de opções
#que leia dois valores e mostre um menu
#[1]somar. [2] multiplicar. [3]maior. [4]novos numeros.[5]sair do programa

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite o segundo numero'))
opcao = 0
while opcao != 5:
    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos numeros')
    print('[5]sair do programa')
    opcao = int(input('qual sua opcao: '))


    if opcao == 1:
        soma = n1 + n2
        print(' a soma de {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('a multipliccao de {} x {} = {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            print('o numero {} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print(' numero {} é menor que {}'.format(n1, n2))
        else:
            print('sao numeros iguais')
    elif opcao == 4:
        n1 = int(input('digite outra opcao: '))
        n2 = int(input('escolha o segundo numero novamente'))
        print('voce escolhou alterar seus numeros {} e {}'.format(n1, n2))
    else:
        print('boa viagem')
    print('=-=-'*10)
print('fim do programa')




