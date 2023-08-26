# O programa cria uma matriz de dimensão 3x3 e preenche com valores lidos pelo teclado, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A Soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

listagemNumeros = list()
somaPares = somaColuna = maiorLinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        listagemNumeros.append(numero)
        if numero % 2 == 0:
            somaPares += numero
        if coluna == 2:
            somaColuna += numero
        if linha == 1 and numero > maiorLinha:
            maiorLinha = numero

print('=-' * 35)
print(f'''
[ {listagemNumeros[0]} ] [ {listagemNumeros[1]} ] [ {listagemNumeros[2]} ]
[ {listagemNumeros[3]} ] [ {listagemNumeros[4]} ] [ {listagemNumeros[5]} ]
[ {listagemNumeros[6]} ] [ {listagemNumeros[7]} ] [ {listagemNumeros[8]} ]
''')
print('=-' * 35)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaColuna}')
print(f'O maior valor da segunda linha é {maiorLinha}')