# Lê o comprimento de 3 retas e determina se podem ou não formar um triângulo.
"""A desigualdade triangular é um princípio que afirma que a soma de dois lados de um triângulo deve ser maior que o
terceiro lado. No código, lemos os comprimentos de três retas (a, b e c) e verificamos se a soma de quaisquer dois lados
é maior que o terceiro, indicando a formação de um triângulo."""

a = float(input('Digite o valor da primeiro segmento: '))
b = float(input('Digite o valor da segundo segmento: '))
c = float(input('Digite o valor da terceiro segmento: '))


if (a + b > c) and (a + c > b) and (b + c > a):
    print('\033[32mOs segmentos acima podem formar um triângulo!\033[m')
else:
    print('\033[31mOs segmentos acima não podem formar um triângulo!\033[m')
