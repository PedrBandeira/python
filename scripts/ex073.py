# O programa lê vários números inteiros e só para quando o usuário digita 999.
# No final mostra a quantidade de números e a soma deles.
soma = quant = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'A soma dos {quant} valores foi {soma}!')