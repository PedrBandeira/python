# Dissecando uma variável
valor = input('Digite algo: ')
print(f"O tipo primitivo desse valor é {type(valor)}")
print(f"Só tem espaços? {valor.isspace()}")
print(f"É um número? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúsculas? {valor.islower()}")
print(f"Está capitalizada? {valor.istitle()}")

"""
# Dissecando uma variável com if, elif e else
valor = input('Digite algo: ')
tipo = 0
# Verificação dos Tipos:
if valor == '':
    tipo = 'NoneType'
    valor = "''"
elif valor.isnumeric():
    tipo = 'Inteiro ou int'
elif valor.replace('.','', 1).isnumeric():
    tipo = 'Float '
elif valor.lower() == 'false' or valor.lower() == 'true':
    tipo = 'Booleano ou bool'
else:
    tipo = 'String'
# Prints
print(f"O tipo primitivo de {valor} é {tipo}")
print(f"Só tem espaços? {valor.isspace()}")
print(f"É um número? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúsculas? {valor.islower()}")
print(f"Está capitalizada? {valor.istitle()}")

"""