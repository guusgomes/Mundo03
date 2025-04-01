from time import sleep
from random import randint

def sorteia(num):
    sleep(0.5)
    print(f'Sorteando {num} valores da lista:', end=' ')
    for n in range(0, num):
        numero = randint(1, 10)
        lista.append(numero)
        print(numero, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    sleep(0.5)
    print(f'Somando os valores pares de {lista}, temos {soma}.')

lista = []
sorteia(5)
somaPar(lista)