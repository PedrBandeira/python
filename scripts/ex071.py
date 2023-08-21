# O programa lê vários números inteiros e só para quando o usuário digitar 999. No final, mostra quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o 999).
num = soma = cont = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')