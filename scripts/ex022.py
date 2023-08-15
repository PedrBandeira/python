# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

# Solicita os nomes dos quatro alunos
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

# Lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Escolhe aleatoriamente um aluno da lista
escolhido = choice(alunos)

# Exibe o nome do aluno escolhido
print(f"Entre os alunos {alunos[0]}, {alunos[1]}, {alunos[2]} e {alunos[3]}, {escolhido} foi escolhido para apagar o quadro.")