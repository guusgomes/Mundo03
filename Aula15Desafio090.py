aluno = {}

aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Media'] = float(input(f'Média de {aluno['Nome']}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'APROVADO'

else:
    aluno['Situação'] = 'REPROVADO'

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')