# O programa joga par ou ímpar com o usuário. Parando somente quando o jogador perder, mostrando o total de vitorias.
from random import randint

cont = 0
while True:
    escolhaUsuario = int(input('Diga um valor: '))
    escolhaPC = randint(0, 10)
    resultado = escolhaUsuario + escolhaPC
    parImpar = ' '
    while parImpar not in 'PI':
        parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {escolhaUsuario} e o computador {escolhaPC}. Total de {resultado}. ', end='')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU ÍMPAR')
    if parImpar == 'P':
        if resultado % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif parImpar == 'I':
        if resultado % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')