tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n = int(input('Digite um número inteiro de 0 a 20: '))

while n < 0 or n > 20:
    n = int(input('Número inválido, digite um número inteiro de 0 a 20: '))

print(f'O número {n} em extenso é {tupla[n]}.') 