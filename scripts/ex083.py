# O programa lê quatro valores e guarda-os em uma tupla. No final mostra:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Você digitou {valores}')
if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes')
else:
    print(f'O valor 9 não foi digitado em nenhuma posição.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')
