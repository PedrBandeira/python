# Este código lê dois números inteiros e mostra a soma entre eles. Em seguida, ele lê dois números reais e também mostra a soma entre esses números.

# Lê dois números inteiros e mostra a soma entre eles.
numInt1 = int(input('Digite o primeiro número: '))
numInt2 = int(input('Digite o segundo número: '))

somaInteiros = numInt1 + numInt2
print(f"A soma entre {numInt1} e {numInt2} é igual à {somaInteiros}")
print('='*50)
#-----------------------------------------------------------------------------------------------------

# Lê dois números reais e mostra a soma entre eles.
numReal1 = float(input('Digite o primeiro número: '))
numReal2 = float(input('Digite o segundo número: '))

somaReais = numReal1 + numReal2
print(f"A soma entre {numReal1} e {numReal2} é igual à {somaReais}")