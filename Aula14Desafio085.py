lista = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        lista[0].append(n) 
    else:
        lista[1].append(n)

print('=' * 60)
print(f'Números pares digitados: {sorted(lista[0])}.')
print(f'Números ímpares digitados: {sorted(lista[1])}.')