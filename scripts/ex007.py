# Este código solicita ao usuário que insira um número inteiro e, em seguida, calcula e exibe o dobro, o triplo e a raiz quadrada desse número. Ele oferece uma maneira prática de obter rapidamente esses cálculos para um valor fornecido.

# Solicita ao usuário para inserir um número inteiro
num = int(input('Digite um número: '))

# Cálcula o dobro, triplo e raiz quadrada do número
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5 # ou 1/2

# Exibe os resultados formatados
print(f"Análise do número {num}:")
print(f"O dobro é {dobro}.")
print(f"O triplo é {triplo}")
print(f"A raiz quadrada  é {raiz:.2f}")