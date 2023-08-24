# O programa contém uma tupla com várias palavras (sem acentos) e mostra, para cada palavra, quais são as suas vogais.

palavras = (
    'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR',
    'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'
)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáãâeéêiíoóôuúû':
            print(letra, end=' ')