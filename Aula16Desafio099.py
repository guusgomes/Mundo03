from time import sleep

def maior(*num):
    cont = len(num)
    maior = 0

    print('=' * 60)
    print('Analisando os valores passados...')

    for n in num:
        if n > maior:
            maior = n

        print(n, end=' ', flush=True)
        
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()