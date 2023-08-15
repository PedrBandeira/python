# Lê um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = int(input('Valor do ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O seno de {angulo}° é igual à {seno:.2f}")
print(f"O cosseno de {angulo}° é igual à {cosseno:.2f}")
print(f"O tangente de {angulo}° é igual à {tangente:.2f}")