# Jogo de Jokenpô, as regras são:
# Pedra vence tesoura;
# Tesoura vence papel;
# Papel vence pedra.

from random import randint

pedra = 1
papel = 2
tesoura = 3

print('--- Jogando Jokenpô ---')
print('Regras:\n'
      'Pedra vence tesoura\n'
      'Tesoura vence papel\n'
      'Papel vence pedra.\n')
escolhaComputador = randint(pedra, tesoura)
print('Escolha um item:\n'
      '[1] Pedra 🪨\n'
      '[2] Papel 📄\n'
      '[3] Tesoura ✂️'
      )
escolhaJogador = int(input('Qual item você escolhe? '))

if 1 <= escolhaJogador <= 3:
    if escolhaComputador == pedra:
        if escolhaJogador == pedra:
            print('EMPATE! Ambos escolheram [1] Pedra 🪨.')
        elif escolhaJogador == papel:
            print('Venceu! Você escolheu [2] Papel 📄 e o computador escolheu [1] Pedra 🪨.')
        else:
            print('Perdeu! Você escolheu [3] Tesoura ✂️ e o computador escolheu [1] Pedra 🪨.')
    elif escolhaComputador == papel:
        if escolhaJogador == pedra:
            print('Perdeu! Você escolheu [1] Pedra 🪨 e o computador escolheu [2] Papel 📄.')
        elif escolhaJogador == papel:
            print('Empate! Ambos escolheram [2] Papel 📄.')
        else:
            print('Venceu! Você escolheu [3] Tesoura ✂️ e o computador escolheu [2] Papel 📄.')
    else: # [3] Tesoura
        if escolhaJogador == pedra:
            print('Venceu! Você escolheu [1] Pedra 🪨 e o computador escolheu [3] Tesoura ✂️.')
        elif escolhaJogador == papel:
            print('Perdeu! Você escolheu [2] Papel 📄 e o computador escolheu [3] Tesoura ✂️.')
        else:
            print('EMPATE! Ambos escolheram [3] Tesoura ✂️.')
else:
    print('Escolha Inválida. Escolha entre [1] Pedra 🪨, [2] Papel 📄 e [3] Tesoura ✂️!')
