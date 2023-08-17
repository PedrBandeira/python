# Programa de Aprovação de Crédito Bancário:
# Calcula o valor da prestação mensal, que não pode passar de 30% do salário ou o emprétimo é negado.
# 1) Valor da casa
# 2) Salário do comprador
# 3) Em quantos anos ele vai pagar
from time import sleep

print('-- Programa de Aprovação de Crédito Bancário --')
valorImovel = float(input('Qual o valor do imóvel desejado? R$'))
salario = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos você pretende quitar o imóvel? '))

quantidadeParcelas = anos * 12
percentualMaximo = salario * 0.30
valorParcelas = valorImovel / quantidadeParcelas

print(
    f"O valor do imóvel é de R${valorImovel:.2f}\n"
    f"Seu salário é de R${salario:.2f} e você pretende quitar o empréstimo em {anos} anos.\n"
    f"ANALISANDO SUA PROPOSTA..."
)
sleep(0.5)
if valorParcelas > percentualMaximo:
    print(f"Empréstimo NEGADO! O valor das parcelas R${valorParcelas:.2f} excede 30% do seu salário R${percentualMaximo:.2f}.")
else:
    print(f"Empréstimo APROVADO! Você conseguiu crédito no valor de R${valorImovel:.2f} para comprar o imóvel desejado.")
    print(f"Você pagará R${valorParcelas:.2f} por {anos} anos ou {quantidadeParcelas} meses.")
