# O programa "pensa" em um número inteiro entre 0 e 10, onde o jogador vai tentar adivinhar até acerta,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint

escolhaPC = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpites = 0
while not acertou:
    escolhaUsuario = int(input('Qual o seu palpite? '))
    palpites += 1
    if escolhaUsuario == escolhaPC:
        acertou = True
    else:
        if escolhaUsuario < escolhaPC:
            print('Mais... Tente mais uma vez.')
        elif escolhaUsuario > escolhaPC:
            print('Menos... Tente mais uma vez.')
print(f"Acertou com {palpites} tentativas. Parabéns!")
