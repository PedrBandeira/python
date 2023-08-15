# Este código converte uma temperatura em graus Celsius para graus Fahrenheit. O usuário fornece a temperatura em Celsius, e o código aplica a fórmula de conversão para calcular o equivalente em Fahrenheit. O resultado é exibido de forma formatada, mostrando a temperatura em ambas as escalas.

# Solicita a temperatura em graus Celsius
celsius = float(input('Informe a temperatura em °C: '))

# Realiza a conversão para Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Exibe o resultado
print(f"A temperatura de {celsius:.2f}°C corresponde a {fahrenheit:.2f}°F")
