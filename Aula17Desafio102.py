def fatorial(num, show):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado;
    :param show: Mostrar ou não o cálculo.
    """
    f = 1
    print(f'{num}! = ', end='')
    if show == 'S':
        for c in range(num, 1, -1):
            print(f'{c}', end=' x ', flush=True)
            f *= c
        print(f'1 = {f}')
    else:
        for c in range(num, 0, -1):
            f *= c
        print(f'{f}.')


n = int(input('Número: '))
opc = str(input('Mostrar processo do cálculo (S/N)? ')).strip().upper()

while opc not in 'SN':
    opc = str(input('Mostrar processo do cálculo (S/N)? ')).strip().upper()

fatorial(n, opc)