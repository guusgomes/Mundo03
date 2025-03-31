ficha = {}
gols = []
somagols = 0

nome = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {nome} jogou? '))

for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))

for g in gols:
    somagols += g

ficha['nome'] = nome
ficha['gols'] = gols
ficha['total'] = somagols

print('=' * 70)
print(ficha)
print('=' * 70)

for k, v in ficha.items():
    print(f'O campo {k} tem o valor: {v}.')

print('=' * 70)

print(f'O jogador {nome} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {somagols} gols.')