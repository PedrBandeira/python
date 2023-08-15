# Este código usa as bibliotecas `math` e `random` do Python para operações matemáticas e números aleatórios. Ele solicita um número ao usuário, gera aleatoriamente um entre 1 e 10 usando `random.randint()`, e executa operações como elevar ao quadrado, calcular raiz quadrada, fatorial, arredondamento e exibe o valor de π (pi). Resultados formatados são mostrados com emojis para uma saída mais amigável.

import math
import random

# Escolhe aleatóriamente um número flutuante entre 1 e 10
numero = random.uniform(1,10)

# Calcula o valor elevado ao quadrado, a raiz quadrada e o fatorial
exponenciacao = math.pow(numero, 2)
raizQuadrada = math.sqrt(numero)
fatorial = math.factorial(int(numero))

# Arredonda para cima (ceil) , para baixo (floor) e para o valor mais próximo
arredondaParaCima = math.ceil(raizQuadrada)
arredondaParaBaixo = math.floor(raizQuadrada)
arredondaParaMaisProximo = round(raizQuadrada)

# Exibe os resultados de forma formatada
print(f"Analisando o número {numero:.2f} com os métodos das bibliotecas Math e Random")
print(f"O valor de {numero:.2f} elevado ao quadrado é {exponenciacao:.2f}")
print(f"A raiz quadrada de {numero:.2f} é igual à {raizQuadrada:.2f}")
print(f"A raiz quadrada arredondada para cima é {arredondaParaCima}")
print(f"A raiz quadrada arredondada para baixo é {arredondaParaBaixo}")
print(f"A raiz quadrada arredondada para o valor mais próximo é {arredondaParaMaisProximo}")
print(f"O valor de {numero:.0f}! é igual à: {fatorial}")