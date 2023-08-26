# O programa recebe 7 valores numéricos, cadastra-os em uma única lista e mantém separados os valores pares e impares.
# No final mostra os valores pares e impares em ordem crescente.

listaNumerica = list()
pares = list()
impares = list()
for cont in range(1, 8):
    numero = int(input(f'Digite o {cont}º valor: '))
    listaNumerica.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

listaNumerica.sort()
print('-=' * 35)
print(f'Os valores digitados foram: {listaNumerica}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valore ímpares digitados foram: {impares}')
