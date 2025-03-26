lista = list()

for n in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {n}: ')))

maior = max(lista)
indicemaiores = []

for imaiores, maiores in enumerate(lista):
    if maiores == maior:
        indicemaiores.append(imaiores)

menor = min(lista)
indicemenores = []

for imenores, menores in enumerate(lista):
    if menores == menor:
        indicemenores.append(imenores)

print(f'Você digitou os números {lista}.')
print(f'O maior número digitado foi {max(lista)} nas posições: {indicemaiores}.')
print(f'O menor número digitado foi {min(lista)} nas posições: {indicemenores}.')