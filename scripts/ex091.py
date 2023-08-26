# O programa lê vários números e coloca em uma lista.
# Depois, cria duas listas extras para conter apenas pares e ímpares digitados. Ao final mostrar o conteúdo das 3 listas

numeros = []
numerosPares = []
numerosImpares = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        if numero % 2 == 0:
            numerosPares.append(numero)
        else:
            numerosImpares.append(numero)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {numerosPares}')
print(f'A lista de ímpares é {numerosImpares}')


