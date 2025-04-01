ficha = {}
gols = []
time = []

while True:
    ficha['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
    gols.clear()

    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))

    ficha['gols'] = gols[:]
    ficha['total'] = sum(gols)
    time.append(ficha.copy())
    resp = str(input('Quer continuar (S/N)? ')).strip().upper()

    while resp not in 'SN':
        resp = str(input('Quer continuar (S/N)? ')).strip().upper()
        
    if resp == 'N':
        break

print('=' * 40)
print('Nº  ', end='')
for i in ficha.keys():
    print(f'{i:<14}', end='')
print()

print('=' * 40)
for k, v in enumerate(time):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()

print('=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    
    if busca == 999:
        break
    
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}.')
    else:
        print(f'    Levantamento do jogador {time[busca]["nome"]}:')
        
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i + 1} fez {g} gols.')
    
    print('=' * 40)
print('FIM')