# Programa lê ano e diz se é bissexto
# Se o ano for divisível por 4 e não for divisível por 100, ele é bissexto.
# No entanto, se o ano for divisível por 100 e não for divisível por 400, ele não é bissexto.
# Se o ano for divisível por 400, ele é bissexto.

ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} É BISSEXTO!")
else:
    print(f"O ano {ano} NÃO É BISSEXTO!")