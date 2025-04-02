from time import sleep

def contador(a, b, c):
    print('=' * 40)
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    sleep(1)

    if c == 0:
        if a < b:
            c = 1
        else:
            c = -1
    elif c < 0: 
        c = -c
    
    if a < b:
        for p in range(a, b + 1, c):
            print(p, end=' ', flush=True)
            sleep(0.5)
    else:
        for p in range(a, b - 1, -c):
            print(p, end=' ', flush=True)
            sleep(0.5)
    
    print('FIM.')


contador(1, 10, 1)
contador(10, 0, 2)

print('=' * 40)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if passo == 0:
    if inicio < fim:
        passo = 1
    else:
        passo = -1

contador(inicio, fim, passo)