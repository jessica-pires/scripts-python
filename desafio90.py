aluno = {}
aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Sua nota: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇAO'
else:
    aluno['situacao'] = 'REPROVADO'
print(f' o aluno {aluno["nome"]} tirou a nota {aluno["media"]} e esta {aluno["situacao"]}')
for k, v in aluno.items():
    print(f'{k} é igual {v}')