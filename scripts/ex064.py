# O programa lê o sexo de uma pessoa, mas só aceita os valores 'M' e 'F'. Caso esteja errado, peça que digite novamente
# até que o valor esteja em 'MmFf'
sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor inválido. Por favor, informe seu sexo: ')).upper().strip()[0]
print(f"Sexo {sexo} registrado com sucesso.")
