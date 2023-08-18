# Lê o peso de 5 pessoas. Depois mostra o maior e o menor peso.

maiorPeso = 0
menorPeso = float('inf')  # Inicializa com um valor infinito

for c in range(0, 5):
    peso = float(input('Digite o peso em kg: '))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso

print(f"O maior peso é {maiorPeso:.2f}kg.")
print(f"O menor peso é {menorPeso:.2f}kg.")
