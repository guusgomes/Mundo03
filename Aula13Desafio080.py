lista = []

for n in range(0, 5):
    numero = int(input('Digite um número: '))
    
    if n == 0 or numero > lista[len(lista) - 1]:
        lista.append(numero)
        print('Adicionado ao fim da lista.')   
    else:
        pos = 0
        
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1

print('=' * 60)
print(f'Os número digitados, em ordem crescente, são: {sorted(lista)}.')