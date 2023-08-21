# Média de notas usando while
nome = str(input('Qual o seu nome? '))
quantidade = int(input('Quantas notas você quer cadastrar? '))
c = 1
somaNotas = 0
while c < (quantidade + 1):
    nota = float(input(f'Digite a {c}ª nota: '))
    somaNotas += nota
    c += 1
media = somaNotas/quantidade
if media >= 7:
    print(f"Olá {nome}, você cadastrou {quantidade} notas e sua média foi {media}. Você foi APROVADO!")
else:
    print(f"Olá {nome}, você cadastrou {quantidade} notas e sua média foi {media}. Você foi REPROVADO!")