# Recebe o salário de um funcionário e calcula o valor do seu aumento.
# Para os inferiores ou iguais o aumento é de 15%
# Para salários superiores a R$1.250, calcule um aumento de 10%

salario = float(input('Qual o valor do seu salário atual em R$? '))

if salario <= 1250:
    valorAumento = salario * 0.15
    salarioAtualizado = salario + valorAumento
    print(f"Seu salário era de R${salario:.2f}, com o aumento de R${valorAumento:.2f} (15% de R${salario:.2f}) ele agora é de R${salarioAtualizado:.2f}")
else:
    valorAumento = salario * 0.10
    salarioAtualizado = salario + valorAumento
    print(f"Seu salário era de R${salario:.2f}, com o aumento de R${valorAumento:.2f} (10% de R${salario:.2f}) ele agora é de R${salarioAtualizado:.2f}")

