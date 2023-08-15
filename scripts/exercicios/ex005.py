# Este código solicita ao usuário que insira dois números e, em seguida, realiza uma série de cálculos aritméticos com esses números. Ele calcula a soma, subtração, multiplicação, exponenciação, divisão, divisão inteira, resto da divisão, raiz quadrada e raiz cúbica dos números fornecidos. Os resultados são apresentados de forma organizada, mostrando os cálculos e seus resultados com duas casas decimais.

# Operadores Aritméticos
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

# Cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
exponenciacao = num1 ** num2
divisao = num1 / num2
divisaoInteira = num1 // num2
resto = num1 % num2
raizQuadrada = num1 ** (1/2)
raizCubica = num1 ** (1/3)

# Resultados
print(f"Resultados para {num1} e {num2}:")

print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Exponenciação: {num1} ** {num2} = {exponenciacao:.2f}") # pow(num1,num2)
print(f"Divisão: {num1} / {num2} = {divisao:.2f}")
print(f"Divisão Inteira: {num1} // {num2} = {divisaoInteira}")
print(f"Resto da Divisão: {num1} % {num2} = {resto}")
print(f"Raiz Quadrada de {num1} é {raizQuadrada:.2f}")
print(f"Raiz Quadrada de {num2} é {raizQuadrada:.2f}")
print(f"Raiz Cúbica de {num1} é {raizCubica:.2f}")
print(f"Raiz Cúbica de {num2} é {raizCubica:.2f}")
print('=' * 30)