# Guarda 5 valores numa lista. No final mostra o maior e o menor valor digitado com sua posição na lista.

valores = []
maior = menor = 0

for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] < menor:
            menor = valores[cont]
        if valores[cont] > maior:
            maior = valores[cont]

print('=-' * 30)
print(f'Você digitou os valores: {valores}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}... ', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}... ', end='')
print()