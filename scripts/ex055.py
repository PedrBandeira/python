# Lê seis números inteiros e mostra a soma apenas daqueles que forem pares.

soma = 0
for c in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f"A soma entre os números pares digitados é {soma}")