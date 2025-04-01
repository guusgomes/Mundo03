def escreva(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


frase = str(input('Digite uma frase: ')).strip()

escreva(frase)