from random import randint
from time import sleep

print('=' * 40)
print(f'{'GERADOR DE JOGOS MEGA SENA':^40}')
print('=' * 40)
n = int(input('Quantos jogos deseja gerar? '))
print('=' * 40)

for c in range(0, n):
    sleep(0.5)
    jogo = []
    for j in range(0, 6):
        jogo.append(randint(1, 60))
    print(f'Jogo {c + 1}: {jogo}.')
    jogo.clear

sleep(0.5)
print('=' * 40)
print(f'{'BOA SORTE!':^40}')
print('=' * 40)