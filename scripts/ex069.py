# Gerador de Progressão Aritmética, lê o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while, ao terminar os 10 termos o programa
# perguntara se o usuário quer mais alguns termos. O programa encerra quando o usuário digitar 0

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, '->', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
