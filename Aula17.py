def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem;
    :param f: Fim da contagem;
    :param p: Passo da contagem;
    :return: Sem retorno.
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c = i

    while c <= f:
        print(f'{c} ', end='', flush=True)
        c += p
    print('FIM!')


help(contador)
print('=' * 60)

def somar (a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: Primeiro valor;
    :param b: Segundo valor;
    :param c: Terceiro valor.
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s = a + b + c
    return s


r1 = somar(b = 4, c = 2)
r2 = somar(3, 2, 5)
r3 = somar(3, 2)
r4 = somar(3)
r5 = somar()

print(f'Os resultados foram {r1}, {r2}, {r3}, {r4} e {r5}.')
print('=' * 60)

def teste(b):
    global a 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}.')
print('=' * 60)

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
print('=' * 60)

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))

if par(num):
    print(f'{num} é PAR.')
else:
    print(f'{num} é ÍMPAR.')

print('=' * 60)