from random import randint
from time import sleep

fichas = []
jogador = {}

print('Valores sorteados: ')

for c in range(1, 5):
    sleep(0.5)
    jogador['numero'] = str(f'jogador {c}')
    jogador['dado'] = randint(1, 6)
    fichas.append(jogador.copy())
    print(f'    O {jogador['numero']} tirou {jogador['dado']}.')

fichas = sorted(fichas, key=lambda item: item['dado'], reverse=True)

sleep(1)
print('Ranking dos jogadores: ')
lugar = 0

for j in fichas:
    sleep(0.5)
    print(f'    {lugar + 1}º lugar: {j['numero']} com {j['dado']}.')
    lugar += 1