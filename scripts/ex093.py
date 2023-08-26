# Recebe nome e idade de 6 pessoas e mostra se é maior ou menor de idade.
galera = list()
dado = list()
totalMaior = totalMenor = 0

for c in range(0, 6):
    dado.append((str(input('Nome: '))))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalMenor += 1
print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade.')