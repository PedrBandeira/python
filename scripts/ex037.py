# Lê três números e mostra qual é o maior e qual é o menor
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))

# Método usado no CursoemVídeo
# Verifica quem é o menor:
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verifica quem é o maior:
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f"Entre os valores {num1}, {num2} e {num3}, o menor é {menor} e o maior é {maior}")

# Esse método coloca as variáveis numa lista, ordena os itens do menor para o maior.
# numeros = sorted([num1, num2, num3])
# menorNumero = numeros[0]
# maiorNumero = numeros[-1]

# print(f"Entre os valores {num1}, {num2} e {num3}, o menor é {menorNumero} e o maior é {maiorNumero}")