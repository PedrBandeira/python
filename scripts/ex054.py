# Tabuada do número digitado pelo usuário com loop for

num = int(input('Digite um número: '))
for c in range(1, 11):
    resultado = num * c
    print(f" {num} × {c} = {resultado}")
