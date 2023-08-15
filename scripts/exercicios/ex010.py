# Este código solicita ao usuário que insira um valor em reais (R$) disponível em sua carteira. Utilizando uma cotação específica do dólar (R$4,96, referente a 15/08/2023), o código converte esse valor em reais para o equivalente em dólares americanos (US$). A saída é uma mensagem formatada que indica o valor em reais inserido pelo usuário e o valor equivalente em dólares com duas casas decimais.

# Solicita o valor em R$ para o usuário
valorEmReais = float(input('Quantos R$ tem na sua carteira?'))
cotacaoDolar = 4.96 # Cotação do dólar em 15/08/2023

# Converte R$ em US$
valorEmDolar = valorEmReais / cotacaoDolar 

# Imprime os valores formatados
print(f"Com R${valorEmReais} você pode comprar US${valorEmDolar:.2f} dólares.")