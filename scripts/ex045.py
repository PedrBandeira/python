# Lê duas notas de um aluno e determina se ele foi aprovado (>=7), está em recuperação (>5<6.9) ou foi reprovado (<=5)

print('--- Calculadora de Médias ---')
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2)/2

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    if media >= 7:
        print(f"A média entre {nota1} e {nota2} é igual à {media}. Sendo maior ou igual à 7, você foi APROVADO!")
    elif 5 <= media <= 6.9:
        print(f"A média entre {nota1} e {nota2} é igual à {media}. "
              f"Sendo menor que 7 e maior que 5, você está em RECUPERAÇÃO!")
    else:
        print(f"A média entre {nota1} e {nota2} é igual à {media}. Sendo menor que 5, você foi REPROVADO!")
else:
    print('A nota deve estar entre 0 e 10. Tente novamente!')
