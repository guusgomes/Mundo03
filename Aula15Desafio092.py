from datetime import date

ficha = {}

ficha['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ficha['Idade'] = date.today().year - nascimento
ficha['Ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))

if ficha['Ctps'] != 0:
    ficha['Contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
    ficha['Aposentadoria'] = ficha['Contratação'] - nascimento + 35

print('=' * 70)

for k, v in ficha.items():
    print(f'{k} tem o valor: {v}.')