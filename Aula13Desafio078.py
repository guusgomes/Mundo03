lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('=' * 60)
print(f'Você digitou os valores {lista}.')

print(f'O maior número digitado foi: {maior} nas posições ', end='')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p} ', end='')

print(f'\nO menor número digitado foi: {menor} nas posições ', end='')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p} ', end='')


#lista = []
#
#for n in range(0, 5):
#    lista.append(int(input(f'Digite um número para a posição {n}: ')))
#
#maior = max(lista)
#indicemaiores = []
#
#for i, maiores in enumerate(lista):
#    if maiores == maior:
#        indicemaiores.append(i)
#
#menor = min(lista)
#indicemenores = []
#
#for i, menores in enumerate(lista):
#    if menores == menor:
#        indicemenores.append(i)
#
#print(f'Você digitou os números {lista}.')
#print(f'O maior número digitado foi {max(lista)} nas posições: {indicemaiores}.')
#print(f'O menor número digitado foi {min(lista)} nas posições: {indicemenores}.')