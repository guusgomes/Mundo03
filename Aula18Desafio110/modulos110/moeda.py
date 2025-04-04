def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if not formato else moeda(res)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxaaum = 10, taxadim = 5):
    print('-' * 35)
    print(f'{'RESUMO DO VALOR':^35}')
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}.')
    print(f'Dobro do preço: \t{dobro(preço, True)}.')
    print(f'Metade do preço: \t{metade(preço, True)}.')
    print(f'{taxaaum}% de aumento: \t{aumentar(preço, taxaaum, True)}.')
    print(f'{taxadim}% de redução: \t{diminuir(preço, taxadim, True)}.')
    print('-' * 35)

