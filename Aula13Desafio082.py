lista = list()
pares = list()
impares = list()

while True: 
    num = int(input('Digite um número: '))

    lista.append(num)

    opcao = str(input('Quer continuar (S/N)? ')).strip().upper()

    if opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar (S/N)? ')).strip().upper()
    
    if opcao == 'N':
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
print(f'Você digitou os números: {lista}.')
print(f'Os números pares digitados foram: {pares}.')
print(f'Os números ímpares digitados foram: {impares}.')