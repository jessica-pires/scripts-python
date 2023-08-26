valor = []

maior = menor = 0


for cont in range(1,6):
    valor.append(int(input(f'digite um valor na posiçao {cont}:  ')))



print(f'Você digitou os valores{valor}')
print(f'O maior valor digitado foi {max(valor)} na posição {valor.index(max(valor))+1}')
print(f'O menor valor digitado foi {min(valor)} na posção {valor.index(min(valor))+1}')

#-------------------------------------------------------------------------------------------
print('------------------------------------------------------------------------------------')





