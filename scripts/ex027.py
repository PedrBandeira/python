# Este código em Python lê um número de 0 a 999 e exibe cada um de seus dígitos separadamente.

numero = input('Digite um número entre 0 e 999: ')
if numero.isdigit() and 0 <= int(numero) <= 999:
    digitos = list(numero)
    print(f"Analisando o número {numero}")
    print(f"Unidade: {digitos[-1]}")
    print(f"Dezena: {digitos[-2]}")
    print(f"Centena: {digitos[-3]}")
else:
    print("Número inválido. Digite um número entre 0 e 999")