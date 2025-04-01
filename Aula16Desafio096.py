def area(a, b):
    areatotal = a * b
    print(f'A área de um terreno {a}x{b} é de {areatotal}m².')


print('CONTROLE DE TERRENOS')
print('=' * 20)

lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(lar, comp)