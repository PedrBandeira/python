# Calcula o IMC conforme o peso e altura dados pelo usuário e mostra seu status:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('--- Calculadora de IMC ---')
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em metros? '))

imc = peso / altura ** 2

if altura > 0 and peso > 0:
    if imc < 18.5:
        print(f"Seu IMC é {imc:.2f} e você está abaixo do peso ideal. Isso indica que você pode estar com insuficiente "
              f"nutrição e precisa focar em uma dieta balanceada.")
    elif 18.5 <= imc < 25:
        print(f"Seu IMC é {imc:.2f} e você está no seu peso ideal. Parabéns, você está saudável e dentro da faixa de "
              f"peso recomendada.")
    elif 25 <= imc < 30:
        print(f"Seu IMC é {imc:.2f} e você está com sobrepeso. Isso indica um risco ligeiramente aumentado para "
              f"problemas de saúde, como diabetes e pressão alta.")
    elif 30 <= imc < 40:
        print(f"Seu IMC é {imc:.2f} e você está com obesidade. Isso indica um risco significativamente aumentado para "
              f"problemas de saúde. Consulte um profissional de saúde para orientação.")
    else:
        print(f"Seu IMC é {imc:.2f} e você está com obesidade mórbida. Isso indica um risco grave para problemas de "
              f"saúde. Procure ajuda médica imediatamente.")
else:
    print('Digite um valor válido!')