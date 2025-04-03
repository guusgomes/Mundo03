def leiaInt(txt):
    print('=' * 40)
    valor = input(f'{txt}')
    
    while valor.isnumeric() == False:
        print('Valor digitado inválido.')
        valor = input(f'{txt}')
        
    return valor
        
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')