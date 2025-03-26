lista = list()
cont = 0

while True: 
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    opcao = str(input('Quer continuar (S/N)? ')).strip().upper()

    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar (S/N)? ')).strip().upper()
    
    if opcao == 'N':
        break

print(f'Os números digitados foram: {lista}.')
print(f'Foram digitados {cont} números.')

if lista.count(5) == 0:
    print('O valor 5 não foi digitado.')
else:
    print(f'O valor 5 foi digitado {lista.count(5)} vez(e)s.')