# Este código solicita ao usuário um número inteiro e, em seguida, apresenta a tabuada desse número utilizando duas formas de repetição: o loop "while" e o loop "for". Primeiro, a tabuada é exibida usando um loop "while", e depois a mesma tabuada é mostrada novamente usando um loop "for". Isso demonstra o uso das diferentes estruturas de repetição disponíveis em Python para realizar a mesma tarefa.

# Solicita ao usuário um número inteiro para mostrar sua tabuada
num = int(input('Digite um número: '))

# Usando o loop while
print(f"Tabuada usando o loop while:")
i = 1
while i <= 10:
    resultado = num * i
    print(f"{num} × {i} = {resultado}")
    i += 1

# Usando o loop for
print("\nTabuada usando o loop for:")
for i in range(1,11):
    resultado = num * i
    print(f"{num} × {i} = {resultado}")