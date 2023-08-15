# Esse programa lê uma frase pelo teclaso e mostra:
# 1 - Quantas vezes aparece a letra 'A';
# 2 - Em que posição ela aparece pela primeira vez;
# 3 - Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

quantidade = frase.count('A')
primeiraPosicao = frase.find('A')
ultimaPosicao = frase.rfind('A')

print(f"A letra 'a' aparece {quantidade} vezes na frase.")
print(f"A primeira ocorrência da letra 'A' foi na posição {primeiraPosicao + 1}.")
print(f"A última ocorrência da letra 'A' foi na posição {ultimaPosicao + 1}.")