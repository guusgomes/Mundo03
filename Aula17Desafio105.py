def notas(*num, sit):
    ficha = {}
    cont = 0
    soma = 0
    maior = num[0]
    menor = num[0]
    
    for c in num:
        cont += 1
        soma += c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    
    media = soma / cont

    ficha['total'] = cont
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['média'] = media

    
    if sit == True:
        situação = ''
        if media < 5:
            situação = 'RUIM'
        elif 5 <= media < 7:
            situação = 'RAZOÁVEL'
        else:
            situação = 'BOA'
        ficha['situação'] = situação
    
    return ficha


resp = notas(7, 7, 7, 7, sit=True)
print(resp)