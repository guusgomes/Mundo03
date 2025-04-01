lista = []
dados = {}
mulheres = []
total = 0
somaidades = 0

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo (M/F): ')).strip().upper()
    
    if sexo == 'F':
        mulheres.append(nome)

    idade = int(input('Idade: '))

    somaidades += idade

    dados['Nome'] = nome
    dados['Sexo'] = sexo
    dados['Idade'] = idade
    lista.append(dados.copy())
    dados.clear
    total += 1

    opc = str(input('Quer continuar (S/N)? ')).strip().upper()

    while opc != 'S' and opc != 'N':
        opc = str(input('Quer continuar (S/N)? ')).strip().upper()

    if opc == 'N':
        break

media = somaidades / total

print('=' * 90)
print(f'- O grupo tem {total} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}.')
print('- A lista das pessoas que estão com idade acima da média:')

for c in lista:
    print('    ', end='')
    if c['Idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')