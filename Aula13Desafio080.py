lista = list()

for n in range(0, 5):
    numero = int(input('Digite um número: '))
    
    if len(lista) == 0:
        lista.append(numero)
        print('Adicionado ao final da lista.')
    
    if len(lista) != 0:
        if len(lista) == 1:
            if numero >= lista[0]:
                lista.append(numero)
                print('Adicionado ao final da lista.')
            if numero < lista[0]:
                lista.insert(0, numero)
                print('Adicionado ao início da lista')

print(lista)