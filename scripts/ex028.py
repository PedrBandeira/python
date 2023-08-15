# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".

cidade = str(input('Qual o nome da cidade? ')).strip()
nomeCidadeSeparada = cidade.upper().split()
if nomeCidadeSeparada[0] == "SANTO":
    print(f"A cidade de '{cidade}' começa com 'SANTO'.")
else:
    print(f"A cidade de '{cidade}' não começa com 'SANTO'.")