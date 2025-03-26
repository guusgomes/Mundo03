lista = []

while True:
    n = int(input('Digite um número: '))

    if lista.count(n) != 0:
        print('Número duplicado, não foi possível adicionar.')
    else: 
        print('Número adicionado.')
        lista.append(n)
    
    opcao = str(input('Quer continuar (S/N)? ')).strip().upper()

    while opcao != 'N' and opcao != 'S':
        opcao = str(input('Quer continuar (S/N)? ')).strip().upper()

    if opcao == 'N':
        break

print(f'Você digitou os números: {sorted(lista)}.')