def notas(*num, sit=False):
    ficha = {}

    ficha['total'] = len(num)
    ficha['maior'] = max(num)
    ficha['menor'] = min(num)
    ficha['média'] = sum(num) / len(num)
    
    if sit:
        situação = ''
        if ficha['média'] < 5:
            situação = 'RUIM'
        elif 5 <= ficha['média'] < 7:
            situação = 'RAZOÁVEL'
        else:
            situação = 'BOA'
        ficha['situação'] = situação
    
    return ficha


resp = notas(7, 6, 5, 4, sit=True)
print(resp)