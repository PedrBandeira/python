# O programa ajuda o jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint, sample
from time import sleep

palpites = list()

print('-' * 60)
print(f"{'JOGO DA MEGA SENA': ^60}")
print('-' * 60)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-' * 60)
print(f"{f'SORTEANDO {jogos} JOGOS': ^60}")
print('-' * 60)
for jogo in range(1, jogos + 1):
    palpites = sample(range(1, 61), 6)
    print(f'Jogo {jogo}: {palpites}')
    sleep(0.5)

print('-' * 60)
print(f"{'BOA SORTE!':^60}")
print('-' * 60)