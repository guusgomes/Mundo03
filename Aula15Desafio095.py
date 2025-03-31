jogadores = []
ficha = {}

while True:

    nome = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    somagols = 0
    gols = []

    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))

    for g in gols:
        somagols += g

    ficha['nome'] = nome
    ficha['gols'] = gols
    ficha['total'] = somagols
    jogadores.append(ficha.copy())
    ficha.clear()

    opc = str(input('Deseja continuar (S/N)? ')).strip().upper()

    while opc != 'N' and opc != 'S':
        opc = str(input('Deseja continuar (S/N)? ')).strip().upper()

    if opc == 'N':
        break

print('=' * 70)
print(f'{'Cód':<4}{'NOME':<15}{'GOLS':<15}{'TOTAL':>6}')
print('-' * 40)

for c in jogadores:
    for v in c.values():
        print(f'{c:<4}{c['nome']:<15}{c['gols']:<15}{c['total']:>6}')


print('=' * 70)


'''print('=' * 70)

print(f'O jogador {nome} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {somagols} gols.')'''