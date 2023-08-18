# Compara dois números inteiros e mostra se ele é maior, menor ou igual.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print(f"Os valores digitados foram: {num1} e {num2}")

if num1 > num2:
    maior = num1
    print(f"O primeiro valor ({num1}) é maior que o segundo ({num2})!")
elif num1 < num2:
    maior = num2
    print(f"O segundo valor ({num2}) é maior que o primeiro ({num1})!")
else:
    print(f"Não existe valor maior, {num1} e {num2} são iguais!")