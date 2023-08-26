# O programa recebe 7 valores numéricos, cadastra-os em uma única lista e mantém separados os valores pares e impares.
# No final mostra os valores pares e impares em ordem crescente.

listaNumerica = [[], []]

for cont in range(1, 8):
    numero = int(input(f'Digite o {cont}º valor: '))
    if numero % 2 == 0:
        listaNumerica[0].append(numero)
    else:
        listaNumerica[1].append(numero)

listaNumerica[0].sort()
listaNumerica[1].sort()

print('-=' * 35)
print(f'Os valores digitados foram: {listaNumerica}')
print(f'Os valores pares digitados foram: {listaNumerica[0]}')
print(f'Os valore ímpares digitados foram: {listaNumerica[1]}')
print('-=' * 35)
