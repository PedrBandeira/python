# Lê o salário do funcionário e mostra o novo salário com 15% de aumento.

# Solicitação do salário
salarioAtual = float(input('Qual o seu salário? R$'))

# Cálculo do aumento e novo salário
percentualDeAumento = 0.15
valorDoAumento = salarioAtual * percentualDeAumento
novoSalario = salarioAtual + valorDoAumento

# Exibição dos resultados formatados
print(f"Seu salário anterior era de R${salarioAtual:.2f}. Com um aumento de 15% sobre o seu salário (equivalente a R${valorDoAumento:.2f}), seu novo salário passa a ser de R${novoSalario:.2f}.")
