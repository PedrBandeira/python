# O programa cadastra vários valores em uma lista. Caso o número já exista na lista, ele não sera adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente
numeros = []
continuar = ''
while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
print('=-' * 30)
print(f'Você digitou os valores {sorted(numeros)}')