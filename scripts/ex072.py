# Programa lê vários números inteiros no final mostra a média entre todos os valor, o maior e o menor valor.
# Parando somente se o usuário digitar 'N'
num = soma = quant = media = maior = menor = 0
continuar = 'Ss'
while continuar not in 'Nn':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma/quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
