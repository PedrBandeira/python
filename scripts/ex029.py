# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nomeCompleto = str(input('Qual o seu nome? ')).strip()
nomeEmLista = nomeCompleto.upper().split()
print(nomeEmLista)
if "SILVA" in nomeEmLista:
    print(f"O nome '{nomeCompleto}' têm 'SILVA' no nome.")
else:
    print(f"O nome '{nomeCompleto}' não têm 'SILVA' no nome.")