# Lê seis números inteiros e mostra a soma apenas daqueles que forem pares.

soma = 0
contador = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}º valor: "))
    if num % 2 == 0:
        soma += num
        contador += 1
print(f"Você informmou {contador} números PARES e a soma deles é {soma}")