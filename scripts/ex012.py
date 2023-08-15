# Este código solicita ao usuário que insira o preço de um produto. Com base no preço fornecido, o código calcula um desconto de 5% sobre o valor original e determina o novo preço com o desconto aplicado. A saída é uma mensagem formatada que apresenta o preço original, o valor do desconto e o preço final com duas casas decimais, proporcionando uma visão clara da economia feita com o desconto.


# Solicita ao usuário o valor do produto
valor = float(input('Qual o preço do produto? '))

# Calcula o desconto (-5%)
porcentagem = 0.05
desconto = valor * porcentagem
valorFinal = valor - desconto

# Exibe o preço original, o desconto e o valor final formatados
print(f"O produto custa R${valor:.2f}, com o desconto de {porcentagem * 100:.0f}% (R${desconto:.2f}), fica por {valorFinal:.2f}")