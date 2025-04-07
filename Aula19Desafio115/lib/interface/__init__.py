def leiaInt(txt):
    while True:
        try:
            valor = int(input(txt))
        
        except (ValueError, TypeError):
            print('\033[31mErro. Valor digitado inválido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar esse dado!')
            return 0

        else:
            return valor


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\33[32mSua opção: \033[m')
    return opc

