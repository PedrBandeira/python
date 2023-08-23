# O programa lê o nome e o preço de vários produtos, perguntando sempre se o usuário quer continuar. Case digite 'N':
# A) Qual o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

totalGasto = totalAcima1000 = precoMaisBarato = cont = 0
produtoMaisBarato = ''
print('-' * 42)
print('----------- LOJA SUPER BARATÃO -----------')
print('-' * 42)
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preco < precoMaisBarato:
        precoMaisBarato = preco
        produtoMaisBarato = nome
    totalGasto += preco
    if preco > 1000:
        totalAcima1000 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'------------ FIM DO PROGRAMA ------------')
print(f'O total da compra foi R$ {totalGasto:.2f}')
print(f'Total de produtos custando mais de R$1.000,00: {totalAcima1000}')
print(f'O produto mais barato foi {produtoMaisBarato} que custa R${precoMaisBarato:.2f}')
