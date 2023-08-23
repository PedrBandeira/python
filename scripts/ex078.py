# O programa simula o funcionamento de um caixa eletrônico.
# Pergunta ao usuário o valor a ser sacado (inteiro) e informa quantas cédulas de cada valor serão entregues
# Considere que o caixa possui células de R$200, R$100, R$50, R$20, R$10, R$5, R$2.

print('=' * 40)
print(f"{'BANCO CEV': ^40}")
print('=' * 40)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 200
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            cel = 0
        totced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')