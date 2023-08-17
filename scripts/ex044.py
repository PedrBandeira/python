# Determina a partir do ano de nascimento digitado pelo usuário se:
# Ele ainda vai se alistar ao serviço militar.
# É hora de se alistar.
# Já passou do tempo do alistamento.
# Em seguida ele mostra o tempo que falta ou que passou do prazo

from datetime import date

print("--- Programa de Alistamento ---")
anoNascimento = int(input('Em qual ano você nasceu? '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
alistamento = 18 - idade

if idade < 18:
    print(f"Você nasceu em {anoNascimento} e fará {idade} anos. Faltam {alistamento} anos para se alistar no serviço militar.")
elif idade > 18:
    print(f"Você nasceu em {anoNascimento} e fará {idade} anos. Passou {abs(alistamento)} anos para se alistar no serviço militar.")
else:
    print(f"Você nasceu em {anoNascimento} e fará {idade} anos. Chegou a hora de se alistar no serviço militar.")