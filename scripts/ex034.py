# Programa lê um número inteiro e mostra se é PAR ou ÍMPAR

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é ÍMPAR!")