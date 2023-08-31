
brasil = []

while True:
    estado = {'uf': str(input('Unidade Federativa: ')), 'sigla': str(input('Sigla do Estado: ')),
              'capital': str(input('Capital da Unidade Federativa: '))}
    brasil.append(estado.copy())

    continuar = input('Deseja adicionar outro estado? [S/N] ').strip().upper()[0]
    if continuar in 'Nn':
        break
    elif continuar != 'S':
        continuar = str(input('Opção inválida! Deseja adicionar outro estado? [S/N] ')).strip().upper()[0]
print('-' * 45)
print(f"{'Unidade':^22} | {'Capital':^22}")
print('-' * 45)
for uf in brasil:
    formatado1 = f"{uf['uf']} - {uf['sigla']}"
    formatado2 = f"{uf['capital']}"
    print(f"{formatado1.center(22)} | {formatado2.center(22)}")
print('-' * 45)