from random import randint

n1 = randint(1,10)
n2 = randint(1,10)
n3 = randint(1,10)
n4 = randint(1,10)
n5 = randint(1,10)
numeros = n1, n2, n3, n4, n5
maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5

print(f'Os números sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')