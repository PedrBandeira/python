# Tabuada do número digitado pelo usuário com loop for

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
for c in range(1, 11):
    resultado = num * c
    print(f" {num} × {c:2} = {resultado}")
print('-' * 15)
