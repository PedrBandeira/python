# Lê vários números e coloca em uma lista. Depois mostra:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) O valor de 5 faz ou não parte da lista
numeros = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
    else:
        print('Valor duplicado! Não vou adicionar')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida. Digite S para Sim ou N para Não.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 20)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 NÃO faz parte da lista!')
