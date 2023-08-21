# Lê o peso de 5 pessoas. Depois mostra o maior e o menor peso.

maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f"O maior peso é {maiorPeso:.2f}kg.")
print(f"O menor peso é {menorPeso:.2f}kg.")
