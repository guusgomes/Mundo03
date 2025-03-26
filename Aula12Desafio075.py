num = int(input('Primeiro número: ')), int(input('Segundo número: ')), int(input('Terceiro número: ')), int(input('Quarto número: '))
pares = ''

print(f'Você digitou os valores {num}.')
print(f'O número 9 foi digitado {num.count(9)} vezes.')

if num.count(3) != 0:
    print(f'O número 3 foi o {num.index(3) + 1}º número digitado.')
else:
    print('O número 3 não apareceu em nenhuma posição.')

for n in num:
    if n % 2 == 0:
        pares = pares + ' ' + str(n) 

print(f'Os números pares digitados foram:{pares}.')


#n1 = int(input('Primeiro número: '))
#n2 = int(input('Segundo número: '))
#n3 = int(input('Terceiro número: '))
#n4 = int(input('Quarto número: '))
#numeros = n1, n2, n3, n4
#pares = ''
#
#if n1 % 2 == 0:
#    pares = pares + ' ' + str(n1)
#if n2 % 2 == 0:
#    pares = pares + ' ' + str(n2)
#if n3 % 2 == 0:
#    pares = pares + ' ' + str(n3) 
#if n4 % 2 == 0:
#    pares = pares + ' ' + str(n4)
#
#print(f'Você digitou os valores: {numeros}.')
#print(f'O valor 9 foi digitado {numeros.count(9)} vezes.')
#
#if numeros.count(3) != 0:
#    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
#else:
#    print('O valor 3 não apareceu em nenhuma posição.')
#
#print(f'Os valores pares digitados foram:{pares}.')