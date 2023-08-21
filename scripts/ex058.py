# Lê uma frase qualquer e diz se ela é um palíndromo (pode ser lido de trás para frente), desconsiderando os espaços.
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
import unidecode
import re

print('-' * 33)
print('--- Analisador de Palíndromos ---')
print('-' * 33)
fraseOriginal = str(input('Digite uma frase: ')).strip().upper()
fraseOriginal = unidecode.unidecode(fraseOriginal)  # Retira os acentos
frase = re.sub(r'[^A-Za-z]', '', fraseOriginal)  # Remove caracteres indesejados
tamanhoFrase = len(frase)

ePalindromo = True  # Supõe que a frase é um palíndromo até ser provado o contrário

print(f"Verificando se a frase '{fraseOriginal}' é um palíndromo...")
print(frase)
print(frase[::-1])

for c in range(tamanhoFrase // 2):
    if frase[c] != frase[tamanhoFrase - 1 - c]:
        ePalindromo = False
        break

if ePalindromo:
    print(f"A frase {fraseOriginal} é um palíndromo!")
else:
    print(f"A frase {fraseOriginal} não é um palíndromo.")

# ou

frase2 = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# ou

frase3 = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
