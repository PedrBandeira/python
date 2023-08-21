# Lê nome, idade e sexo de 4 pessoas. No final mostra:
# A média de idade do grupo
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
media = 0
nomeHomemVelho = ''
idadeHomemVelho = 0
mulheresMenos20 = 0

for c in range(1, 5):
    print(f"----- {c}ª PESSOA -----")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    if c == 1 and sexo in 'Mm':
        nomeHomemVelho = nome
        idadeHomemVelho = idade
    if sexo in 'Mm' and idade > idadeHomemVelho:
        nomeHomemVelho = nome
        idadeHomemVelho = idade
    if sexo in 'Ff' and idade < 20:
        mulheresMenos20 += 1
mediaFinal = media/4
print(f"A média de idade do grupo é de {mediaFinal} anos")
print(f"O homem mais velho tem {idadeHomemVelho} anos e se chama {nomeHomemVelho}")
print(f"Ao todo são {mulheresMenos20} mulheres com menos de 20 anos.")