lista = list()

while True: 
    n = int(input('Digite um número: '))
    lista.append(n)
    opcao = str(input('Quer continuar (S/N)? ')).strip().upper()

    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar (S/N)? ')).strip().upper()
    
    if opcao == 'N':
        break

print(f'Os números digitados foram: {sorted(lista, reverse=True)}.')
print(f'Foram digitados {len(lista)} números.')

if lista.count(5) == 0:
    print('O valor 5 não foi digitado.')
else:
    print(f'O valor 5 foi digitado {lista.count(5)} vez(es).')