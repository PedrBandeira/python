# Lê um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians

angulo = float(input('Valor do ângulo: '))
angulo = radians(angulo)

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print(f"O seno de {angulo:.2f}° é igual à {seno:.2f}")
print(f"O cosseno de {angulo:.2f}° é igual à {cosseno:.2f}")
print(f"O tangente de {angulo:.2f}° é igual à {tangente:.2f}")