linha = []

for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [0, {n}]: ')))

for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [1, {n}]: ')))

for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [2, {n}]: ')))

formatada = sorted(linha)

print(formatada[:3])
print(formatada[3:6])
print(formatada[6:])