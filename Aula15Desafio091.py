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
    print(f'    O {jogador["numero"]} tirou {jogador["dado"]}.')

fichas = sorted(fichas, key=lambda item: item['dado'], reverse=True)

sleep(1)
print('Ranking dos jogadores: ')

for k, v in enumerate(fichas):
    sleep(0.5)
    print(f'    {k + 1}º lugar: {v["numero"]} com {v["dado"]}.')