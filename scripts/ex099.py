# Lê o nome e duas notas de vários alunos e guarda tudo em uma lista composta. No final:
# Mostra o boletim contendo a média de cada um e # permite que o usuário possa mostrar as notas de cada aluno.

listaAlunos = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    notas = [nota1, nota2]
    aluno = [nome, media, notas]
    listaAlunos.append(aluno)

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = input('Opção inválida. Deseja continuar? [S/N] ').strip().upper()[0]

print('=-' * 30)
print(f"{'Nº':<4}{'NOME':<15}{'MÉDIA':>6}")
print('=-' * 30)

for numero, aluno in enumerate(listaAlunos):
    print(f"{numero:<4}{aluno[0]:<15}{aluno[1]:>6.1f}")

print('=-' * 30)

while True:
    mostrar = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'Notas de {listaAlunos[mostrar][0]} são {listaAlunos[mostrar][2]}')
