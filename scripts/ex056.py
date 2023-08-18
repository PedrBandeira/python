# Lê o primeiro termo e a razão de uma PA (Progressão Aritmética) e mostra os 10 primeiros termos dessa progressão
from time import sleep

print('-' * 51)
print('--- Calculando uma P.A. (Progressão Aritmética) ---')
print('-' * 51)
termoInicial = int(input('Digite o primeiro termo da sequência: '))
razao = int(input('Digite a razão (diferença constante) da sequência: '))
enezimoTermo = 10
print('-' * 51)
print("Os 10 primeiros termos da progressão são:")
for c in range(enezimoTermo):
    print(termoInicial, end=" ")
    termoInicial += razao
    sleep(0.2)
