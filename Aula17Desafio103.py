def ficha(n = 'desconhecido', g = 0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('=' * 40)
nome = str(input('Nome do jogador: '))
gols = int(input('Número de gols: '))

if gols == '':
    gols = 0

ficha(nome, gols)