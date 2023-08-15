# import math
from math import pow, sqrt, factorial, ceil
num = int(input('Digite um número: '))
pot = pow(num,2) # pot = math.pow(num, 2)
raiz = sqrt(num) # raiz = math.sqrt(num)
fat = factorial(num) # fat = math.factorial(num)
print(f"O valor de {num} elevado ao quadrado é {pot}")
print(f"A raiz quadrada de {num} é {raiz:.2f}")
print(f"A raiz quadrada arredondada para cima de {num} é {ceil(raiz)}")
print(f"O fatorial de {num} é {fat}")