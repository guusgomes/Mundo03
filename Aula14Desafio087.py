linha = []
for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [0, {n}]: ')))
for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [1, {n}]: ')))
for n in range(0, 3):
    linha.append(int(input(f'Digite o valor para [2, {n}]: ')))

print('=' * 60)
print(linha[:3])
print(linha[3:6])
print(linha[6:])
print('=' * 60)

somapares = 0
for n in linha:
    if n % 2 == 0:
        somapares += n
print(f'A soma dos números pares é: {somapares}.')

soma3coluna = 0
for n in linha[2::3]:
    soma3coluna += n
print(f'A soma dos números da terceira coluna é: {soma3coluna}.')

print(f'O maior valor da segunda linha é {max(linha[3:6])}.')