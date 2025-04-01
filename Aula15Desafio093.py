ficha = {}
gols = []

ficha['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))

for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))

ficha['gols'] = gols
ficha['total'] = sum(gols)

print('=' * 70)
print(ficha)
print('=' * 70)

for k, v in ficha.items():
    print(f'O campo {k} tem o valor: {v}.')

print('=' * 70)

print(f'O jogador {ficha["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {ficha["total"]} gols.')