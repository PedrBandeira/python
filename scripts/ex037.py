# Lê três números e mostra qual é o maior e qual é o menor

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
numeros = sorted([num1, num2, num3])
menorNumero = numeros[0]
maiorNumero = numeros[-1]

print(f"Entre os valores {num1},{num2} e {num3}, o menor é {menorNumero} e o maior é {maiorNumero}")