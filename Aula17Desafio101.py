def voto(n):
    from datetime import date

    idade = date.today().year - nasc
    
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade == 16 or idade == 17 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


print('=' * 60)
nasc = int(input('Em que ano você nasceu? '))

voto(nasc)