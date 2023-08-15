# Este código solicita ao usuário que insira um número inteiro e, em seguida, calcula e exibe na tela o sucessor e o antecessor desse número. Ele oferece uma maneira rápida de visualizar os números imediatamente seguintes e anteriores ao número inserido.

# Solicita o número ao usuário
num = int(input('Digite um número: '))

# Calcula o sucessor e antecessr
sucessor = num + 1
antecessor = num - 1

# Exibe os resultados
print(f"Para o número {num}, seu sucessor é {sucessor} e seu antecessor é {antecessor}.")
