# Jogo de Jokenpô

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('--- Jogando Jokenpô ---')
print('Regras:\n'
      'Pedra vence tesoura\n'
      'Tesoura vence papel\n'
      'Papel vence pedra.\n')
escolhaComputador = randint(0, 2)
print('Escolha um item:\n'
      '[0] Pedra 🪨\n'
      '[1] Papel 📄\n'
      '[2] Tesoura ✂️'
      )
escolhaJogador = int(input('Qual item você escolhe? '))

print('JO')
sleep(0.2)
print('KEN')
sleep(0.2)
print('PÔ')
sleep(0.2)

if 0 <= escolhaJogador <= 2:
    if escolhaComputador == 0:
        if escolhaJogador == 0:
            print('EMPATE! Ambos escolheram [0] Pedra 🪨.')
        elif escolhaJogador == 1:
            print('Venceu! Você escolheu [1] Papel 📄 e o computador escolheu [0] Pedra 🪨.')
        else:
            print('Perdeu! Você escolheu [2] Tesoura ✂️ e o computador escolheu [0] Pedra 🪨.')
    elif escolhaComputador == 1:
        if escolhaJogador == 0:
            print('Perdeu! Você escolheu [0] Pedra 🪨 e o computador escolheu [1] Papel 📄.')
        elif escolhaJogador == 1:
            print('Empate! Ambos escolheram [1] Papel 📄.')
        else:
            print('Venceu! Você escolheu [2] Tesoura ✂️ e o computador escolheu [1] Papel 📄.')
    else: # [3] Tesoura
        if escolhaJogador == 0:
            print('Venceu! Você escolheu [0] Pedra 🪨 e o computador escolheu [2] Tesoura ✂️.')
        elif escolhaJogador == 1:
            print('Perdeu! Você escolheu [1] Papel 📄 e o computador escolheu [2] Tesoura ✂️.')
        else:
            print('EMPATE! Ambos escolheram [2] Tesoura ✂️.')
else:
    print('Escolha Inválida. Escolha entre [0] Pedra 🪨, [1] Papel 📄 e [2] Tesoura ✂️!')
