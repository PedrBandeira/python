# Programa lê ano e diz se é bissexto
# Se o ano for divisível por 4 e não for divisível por 100, ele é bissexto.
# No entanto, se o ano for divisível por 100 e não for divisível por 400, ele não é bissexto.
# Se o ano for divisível por 400, ele é bissexto.
from datetime import date

ano = int(input('Digite o ano: '))

# Se o usuário digitou 0, o ano recebe o valor do ano atual
if ano == 0:
    ano = date.today().year

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} É BISSEXTO!")
else:
    print(f"O ano {ano} NÃO É BISSEXTO!")
