# O programa cria uma matriz de dimensão 3x3 e preenche com valores lidos pelo teclado
listagemNumeros = list()
for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        listagemNumeros.append(numero)

print(f'''[ {listagemNumeros[0]} ] [ {listagemNumeros[1]} ] [ {listagemNumeros[2]} ]
[ {listagemNumeros[3]} ] [ {listagemNumeros[4]} ] [ {listagemNumeros[5]} ]
[ {listagemNumeros[6]} ] [ {listagemNumeros[7]} ] [ {listagemNumeros[8]} ]
''')