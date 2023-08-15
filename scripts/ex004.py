# Este código solicita que o usuário insira um valor e, em seguida, realiza uma análise detalhada desse valor. Ele verifica o tipo primitivo do valor e exibe informações sobre suas características, como se contém apenas espaços, se é numérico, alfabético, alfanumérico, se está em maiúsculas, minúsculas ou capitalizado. O código também inclui verificações condicionais para determinar o tipo do valor e fornece respostas específicas para cada caso.

# Dissecando uma variável:
valor = input('Digite algo: ')

# Verificação dos Tipos:
if valor == '':
    tipo = 'NoneType'
    valor = "''"
elif valor.isnumeric():
    tipo = 'Inteiro'
elif valor.replace('.', '', 1).isnumeric():
    tipo = 'Float'
elif valor.lower() == 'false' or valor.lower() == 'true':
    tipo = 'Booleano'
else:
    tipo = 'String'

# Prints
print(f"O tipo primitivo de {valor} é {tipo}")
print(f"Só tem espaços? {valor.isspace()}")
print(f"É um número? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúscula? {valor.islower()}")
print(f"Está capitalizada? {valor.istitle()}")