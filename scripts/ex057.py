# Determina se o número inteiro digitado é primo ou não

print('-' * 109)
print('-' * 38, ' Verificador de Números Primos ', '-' * 38)
print('Um número primo é um número inteiro maior que 1 que possui apenas dois divisores diferentes: 1 e ele mesmo')
print('-' * 109)
numero = int(input('Digite um número: '))
totalDivisiveis = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', c, end=' ')
        totalDivisiveis += 1
    else:
        print('\033[31m', c, end=' ')
print(f"\n\033[mO número {numero} foi divisível {totalDivisiveis} vezes")
if totalDivisiveis == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
