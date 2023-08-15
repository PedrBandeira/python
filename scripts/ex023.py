# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome de quatro alunos e mostre na ordem sorteada.
from random import shuffle

# Solicita os nomes dos quatro alunos
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

# Insere os nomes dos alunos em um Array
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a ordem dos alunos na lista
shuffle(alunos)

# Exibe a ordem de apresentação dos trabalhos
print(f"Ordem de apresentação dos trabalhos:")
for indice, aluno in enumerate(alunos, start=1):
    print(f"{indice}º a apresentar é: {aluno}")