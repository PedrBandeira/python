# Lê o comprimento de 3 retas e determina se podem ou não formar um triângulo.
"""A desigualdade triangular é um princípio que afirma que a soma de dois lados de um triângulo deve ser maior que o
terceiro lado. No código, lemos os comprimentos de três retas (a, b e c) e verificamos se a soma de quaisquer dois lados
é maior que o terceiro, indicando a formação de um triângulo."""

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))


if (a + b > c) and (a + c > b) and (b + c > a):
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!')
