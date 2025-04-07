def leiaInt(txt):
    while True:
        try:
            valor = int(input(txt))
        
        except (ValueError, TypeError):
            print('Erro. Valor digitado inválido.')
            continue

        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar esse dado!')
            return 0

        else:
            return valor


def leiaFloat(txt):
    while True:
        try:
            valor = float(input(txt))
        
        except (ValueError, TypeError):
            print('Erro. Valor digitado inválido.')
            continue

        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar os dados!')
            return 0
        
        else:
            return valor
        

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')

print('=' * 45)
print(f'O número inteiro digitado foi {inteiro} e o real {real}.')