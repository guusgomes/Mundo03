listagem = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 15.90, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'RS {listagem[pos]:>6.2f}')

print('-' * 40)


#listagem = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 15.90, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
#
#print('-' * 30)
#print(' '* 5, 'LISTAGEM DE PREÇOS', ' ' * 5)
#print('-' * 30)
#print(f'{listagem[0]}................R$   {listagem[1]:.2f}')
#print(f'{listagem[2]}.............R$   {listagem[3]:.2f}')
#print(f'{listagem[4]}..............R$  {listagem[5]:.2f}')
#print(f'{listagem[6]}...............R$  {listagem[7]:.2f}')
#print(f'{listagem[8]}.........R$   {listagem[9]:.2f}')
#print(f'{listagem[10]}.............R$   {listagem[11]:.2f}')
#print(f'{listagem[12]}..............R$ {listagem[13]:.2f}')
#print(f'{listagem[14]}..............R$  {listagem[15]:.2f}')
#print(f'{listagem[16]}................R$  {listagem[17]:.2f}')
#print('-' * 30)