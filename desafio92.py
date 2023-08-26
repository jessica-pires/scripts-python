from datetime import datetime
dados = {}
dados['nome:'] = input('Digite seu nome: ')
nasci = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasci
dados['carteira'] = int(input('Carteira de trabalho:[0 nao tem] '))
if dados['carteira'] != 0:
        dados['contratacao'] = int(input('ano de contratacao: '))
        dados['salario'] = int(input('seu salario'))
        dados['aposentadoria'] = dados['contratacao'] + 35
#print(dados)
for k, v in dados.items():
    print(f'{k} :{v}')




