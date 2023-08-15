# Lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e mostra o comprimento da hipotenusa
from math import pow, sqrt

# Solicita o comprimento do cateto oposto e do cateto adjacente
catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

# Calcula o comprimento da hipotenusa usando o teorema de Pitágoras
hipotenusa = sqrt(pow(catetoOposto,2) + pow(catetoAdjacente,2))

# Exibe o comprimento da hipotenusa
print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")