# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nomeCompleto = str(input('Qual o seu nome? ')).strip()

nomeEmLista = nomeCompleto.split()
primeiroNome = nomeEmLista[0]
ultimoNome = nomeEmLista[-1]

print(f"Seu nome é: {nomeCompleto}")
print(f"Primeiro nome: {primeiroNome}")
print(f"Último nome: {ultimoNome}")