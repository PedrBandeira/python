# Este código solicita ao usuário o nome do aluno, bem como duas notas. Com base nas notas fornecidas, calcula a média aritmética entre elas e determina se o aluno foi aprovado ou reprovado. Caso a média seja maior ou igual a 7, o aluno é considerado aprovado; caso contrário, é considerado reprovado. A saída exibe uma mensagem personalizada com o nome do aluno, as notas, a média calculada e o status (aprovado ou reprovado).


# Solicita o nome do aluno
nome = input('Qual é o seu nome? ')

# Lê as notas (float para permitir casas decimais)
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

# Calcula a média
media = (nota1 + nota2) / 2

# Verifica se o aluno foi aprovado ou reprovado
status = 'APROVADO' if media >= 7 else 'REPROVADO'

# Exibe a mensagem formatada
print(f"Olá, {nome}. A média entre {nota1} e {nota2} é {media:.2f} e você foi {status}.")
