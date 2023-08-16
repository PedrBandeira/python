# O programa escolhe um número inteiro entre 0 e 5 e pede para que o usuário advinhe qual foi o valor escolhido.
# O programa escreve na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
print('=' * 87)
print('Vou pensar em um número inteiro entre 0 e 5. Consegue adivinhar qual número eu escolhi?')
valorEscolhido = randint(0,5)
# print(f"Pensei no valor {valorEscolhido}")

valorDoUsuario = int(input('Qual valor, entre 0 e 5, o programa escolheu? '))

if valorDoUsuario >= 0 and valorDoUsuario <=5:
    print('\033[93mPROCESSANDO...')
    sleep(1)
    if valorDoUsuario == valorEscolhido:
        print(f"\033[92mParábens, você acertou!! Você e o programa escolheram o número {valorEscolhido}!")
    else:
        print(f"\033[91mQue pena, você errou!! Você escolheu o número {valorDoUsuario} e o programa escolheu o número {valorEscolhido}!")
else:
    print(f"\033[91mO valor {valorDoUsuario} não está entre 0 e 5. Por favor insira um valor válido!")