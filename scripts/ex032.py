# O programa escolhe um número inteiro entre 0 e 5 e pede para que o usuário advinhe qual foi o valor escolhido.
# O programa escreve na tela se o usuário venceu ou perdeu
from random import randint
valorEscolhido = randint(0,5)
# print(valorEscolhido)
valorDoUsuario = int(input('Qual valor o programa escolheu entre 0 e 5? '))
if valorDoUsuario == valorEscolhido:
    print(f"Parábens, você acertou!! Você e o programa escolheram o número {valorEscolhido}!")
else:
    print(f"Que pena, você errou!! Você escolheu o número {valorDoUsuario} e o programa escolheu o número {valorEscolhido}!")