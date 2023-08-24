# Gera cinco números aleatórios e os coloca em uma tupla. Depois mostra os números gerados, o maior e o menor.

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')

for num in numeros:
    print(f'{num} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
