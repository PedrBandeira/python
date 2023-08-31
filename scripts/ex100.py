locadora = []

while True:
    print('-' * 30)
    titulo = str(input('Qual o título do filme? '))
    ano = int(input('Em qual ano foi lançado? '))
    diretor = str(input('Quem foi o diretor? '))
    print('-' * 30)

    filme = {"titulo": titulo, "ano": ano, "diretor": diretor}
    locadora.append(filme)

    continuar = input('Deseja adicionar outro filme? [S/N] ').strip().upper()[0]
    if continuar in 'Nn':
        break
    elif continuar != 'S':
        continuar = str(input('Opção inválida! Deseja adicionar outro filme? [S/N] ')).strip().upper()[0]

print('-' * 60)
print(f"{'Filmes Cadastrados:' :^60}")
print('-' * 60)
for film in locadora:
    print(f'- {film["titulo"]} de {film["ano"]} dirigido por {film["diretor"]} [DISPONÍVEL]')
