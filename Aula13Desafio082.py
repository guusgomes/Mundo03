lista = list()
pares = list()
impares = list()

while True: 
    n = int(input('Digite um número: '))

    lista.append(n)

    opcao = str(input('Quer continuar (S/N)? ')).strip().upper()

    if opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar (S/N)? ')).strip().upper()
    
    if opcao == 'N':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    
print(f'Você digitou os números: {lista}.')
print(f'Os números pares digitados foram: {pares}.')
print(f'Os números ímpares digitados foram: {impares}')