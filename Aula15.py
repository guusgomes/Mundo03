'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

pessoas['peso'] = 98

for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])'''

estado = {}
brasil = []

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    '''for k, v in e.items():
        print(f'{k} = {v}')'''
    for v in e.values():
        print(v, end=' ')
    print()