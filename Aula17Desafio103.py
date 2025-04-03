def ficha(n, g):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('=' * 40)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))

if nome == '':
    nome = 'desconhecido'

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)