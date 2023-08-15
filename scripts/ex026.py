# Este programa lê o nome completo de uma pessoa e realiza as seguintes tarefas:
# 1) Converte o nome para maiúsculas e o imprime.
# 2) Converte o nome para minúsculas e o imprime.
# 3) Calcula a quantidade total de letras no nome, desconsiderando os espaços, e a imprime.
# 4) Calcula a quantidade de letras no primeiro nome e a imprime.

nomeCompleto = str(input('Digite o seu nome completo: ')).strip()

quantidadeDeLetras = len(nomeCompleto.replace(" ", ""))
nomeArray = nomeCompleto.split()

print(f"Seu nome completo em maiúsculas é: '{nomeCompleto.upper()}'")
print(f"Seu nome completo em minúsculas é: '{nomeCompleto.lower()}'")
print(f"Seu nome tem, sem considerar os espaços, {quantidadeDeLetras} letras!")
print(f"Seu primeiro nome é {nomeArray[0]} e tem {len(nomeArray[0])} letras!")
