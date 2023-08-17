# Converte um número inteiro digitado pelo usuário para binário, octal ou hexadecimal

print('--- Programa de Base de Conversão ---')

numero = int(input('Digite um número para conversão: '))
print('Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
base = int(input('Digite a opção desejada [1/2/3]: '))

if 1 <= base <= 3:
    if base == 1:
        numeroConvertido = (bin(numero)[2:]).upper()
        print(f'O número digitado foi {numero}, a base de conversão escolhida foi [1] binário, '
              f'o resultado da conversão é: {numeroConvertido}')
    elif base == 2:
        numeroConvertido = oct(numero)[2:].upper()
        print(f'O número digitado foi {numero}, a base de conversão escolhida foi [2] octal, '
              f'o resultado da conversão é: {numeroConvertido}')
    elif base == 3:
        numeroConvertido = hex(numero)[2:].upper()
        print(f'O número digitado foi {numero}, a base de conversão escolhida foi [3] hexadecimal, '
              f'o resultado da conversão é: {numeroConvertido}')
else:
    print('OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA ENTRE [1], [2] E [3]!')