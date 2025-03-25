palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'

for palavra in palavras:
    vogais = ' '.join([letra for letra in palavra if letra.lower() in 'aeiou'])
    print(f'A palavra {palavra.upper()} tem as vogais: {vogais.upper()}.')