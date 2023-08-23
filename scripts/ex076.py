# O programa lê a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada o programa deverá perguntar se o usuário quer continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

total18 = mulheres20 = homens = 0
while True:
    print('-' * 41)
    print('-' * 9,' CADASTRE UMA PESSOA ','-' * 9)
    print('-' * 41)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-' * 41)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 41)
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres20}')
print('-' * 41)
