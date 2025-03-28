linha = []

for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [0, {n}]: ')))

for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [1, {n}]: ')))

for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [2, {n}]: ')))

print('=' * 60)
print(f'[ {linha[0]:^6} ][ {linha[1]:^6} ][ {linha[2]:^6} ]')
print(f'[ {linha[3]:^6} ][ {linha[4]:^6} ][ {linha[5]:^6} ]')
print(f'[ {linha[6]:^6} ][ {linha[7]:^6} ][ {linha[8]:^6} ]')