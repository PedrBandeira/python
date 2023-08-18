# Lê o ano de nascimento de 7 pessoas e no final, mostra:
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

totalMaioridade = 0
totalMenoridade = 0
for c in range(0,7):
    anoNascimento = int(input('Digite o ano de nascimento: '))
    anoAtual = date.today().year
    idade = abs(anoAtual - anoNascimento)
    if idade >= 18:
        totalMaioridade += 1
    else:
        totalMenoridade += 1
print(f"De 7 idades analisadas, "
      f"{totalMaioridade} já atingiram a maioridade e "
      f"{totalMenoridade} ainda não atingiram a maioridade.")