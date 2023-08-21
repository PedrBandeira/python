# O programa lê dois valores e mostra o seguinte menu:
# [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa
from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
    ''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        resultado = num1 + num2
        print(f"A soma entre {num1} e {num2} é igual à {resultado}")
    elif opcao == 2:
        resultado = num1 * num2
        print(f"O produto de {num1} x {num2} é igual à {resultado}")
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        elif num1 < num2:
            maior = num2
        else:
            print(f"Os números {num1} e {num2} são iguais!")
        print(f"Entre {num1} e {num2} o maior valor é {maior}")
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-' * 20)
    sleep(0.5)
print('Fim do programa! Volte sempre!')