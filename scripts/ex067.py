# O programa lê um número e mostra o seu fatorial
'''
from math import factorial
num = int(input('Digite um número para calcular o seu Fatorial: '))
fat = factorial(num)
print(f'O fatorial de {num} é {fat}.')
'''

# ou

num = int(input('Digite um número para calcular o seu Fatorial: '))
contador = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)
