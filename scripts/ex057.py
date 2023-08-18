# Determina se o número inteiro digitado é primo ou não

print('-' * 109)
print('-' * 38, ' Verificador de Números Primos ', '-' * 38)
print('Um número primo é um número inteiro maior que 1 que possui apenas dois divisores diferentes: 1 e ele mesmo')
print('-' * 109)
numero = int(input('Digite um número: '))
if numero < 2:
    print(f"{numero} não é um número primo.")
elif numero == 2:
    print(f"2 é um número é primo.")
else:
    primo = True
    for c in range(2, int(numero ** 0.5) + 1):
        if numero % c == 0:
            primo = False
            break
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
