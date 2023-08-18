# Mostra todos os números pares entre 1 e 50:

print('Lista de número pares entre 1 e 50')
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=" ")
# ou
print('\n',('-' * 66))
for c in range(2, 51, 2):  # Preferencial pois exige menos processamento
    print(c, end=" ")
