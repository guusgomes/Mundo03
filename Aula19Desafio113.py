def leiaInt(txt):
    while True:
        try:
            valor = int(input(f'{txt}'))
            break
        
        except (ValueError, TypeError):
            print('Erro. Tipo de dado digitado inválido.')

        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
        
    return valor


def leiaFloat(txt):
    while True:
        try:
            valor = float(input(f'{txt}'))
            break
        
        except (ValueError, TypeError):
            print('Erro. Tipo de dado digitado inválido.')

        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
        
    return valor
        

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')

print('=' * 45)
print(f'O número inteiro digitado foi {inteiro} e o real {real}.')