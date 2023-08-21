# O programa lê um número inteiro qualquer e mostra na tela uma quantidade definida pelo usuário dos
# primeiros elementos de uma Sequência de Fibonacci

print('-' * 30)
print('Sequência Fibonacci')
num = int(input('Quantos termos você quer mostrar? '))
primeiroTermo = 0
segundoTermo = 1
print(f'{primeiroTermo} -> {segundoTermo}', end='')
cont = 3
while cont <= num:
    terceiroTermo = primeiroTermo + segundoTermo
    print(f' -> {terceiroTermo}', end='')
    primeiroTermo = segundoTermo
    segundoTermo = terceiroTermo
    cont += 1
print(' -> Fim')

