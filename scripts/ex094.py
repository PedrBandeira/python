# O programa lê nome e peso de várias pessoas, guardando tudo em uma lista. No final mostra:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dado = list()
pessoas = list()
pessoasPesadas = list()
pessoasLeves = list()
maiorPeso = menorPeso = total = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso (kg): ')))
    pessoas.append(dado[:])
    dado.clear()
    total += 1

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = input('Opção inválida. Deseja continuar? [S/N] ').strip().upper()[0]

print(f'Ao todo, você cadastrou {total} pessoas.')
for pessoa in pessoas:
    nome, peso = pessoa
    if peso > maiorPeso:
        maiorPeso = peso
        pessoasPesadas = [nome]
    elif peso == maiorPeso:
        pessoasPesadas.append(nome)

    if peso < menorPeso or menorPeso == 0:
        menorPeso = peso
        pessoasLeves = [nome]
    elif peso == menorPeso:
        pessoasLeves.append(nome)

print(f'O maior peso foi de {maiorPeso:.2f}kg. {pessoasPesadas}')
print(f'O menor peso foi de {menorPeso:.2f}kg {pessoasLeves}')

