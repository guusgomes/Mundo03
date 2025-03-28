ficha = []

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2

    ficha.append([nome, [n1, n2], media])
    opcao = str(input('Quer continuar (S/N)? ')).strip()
    if opcao in 'Nn':
        break

print('=' * 30)
print(f'{'No.':<4}{'NOME':<13}{'MÉDIA':>13}')
print('=' * 30)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<13}{a[2]:>13}')


print('=' * 30)

while True:
    qualaluno = int(input('Mostrar notas de qual aluno (999 p/ sair)? '))

    if qualaluno == 999:
        break

    print(f'Notas de {ficha[qualaluno][0]}: {ficha[qualaluno][1]}.')
    print('=' * 30)

print('=' * 30)
print('FIM')


'''
alunos = []
notas = []

while True:
    notas.append(str(input('Nome: ')).strip().capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    notas.clear()

    opcao = str(input('Quer continuar (S/N)? ')).strip().upper()
    
    if opcao == 'N':
        break

print('=' * 30)
print(f'{'No.':<4}', end='')
print(f'{'NOME':<13}', end='')
print(F'{'MÉDIA':>13}')
print('=' * 30)

for a in range(0, len(alunos)):
    print(f'{a:<4}', end='')
    print(f'{alunos[a][0]:<13}', end='')
    print(f'{((alunos[a][1] + alunos[a][2]) / 2):>13.1f}')

print('=' * 30)

while True:
    qualaluno = int(input('Mostrar notas de qual aluno (999 p/ sair)? '))

    if qualaluno == 999:
        break

    print(f'Notas de {alunos[qualaluno][0]}: {alunos[qualaluno][1]} e {alunos[qualaluno][2]}.')
    print('=' * 30)

print('=' * 30)
print('FIM')
'''