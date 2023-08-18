# Determina a partir do ano de nascimento digitado pelo usuário se:
# Ele ainda vai se alistar ao serviço militar.
# É hora de se alistar.
# Já passou do tempo do alistamento.
# Em seguida ele mostra o tempo que falta ou que passou do prazo

from datetime import date

masculino = 1
feminino = 2

print("--- Programa de Alistamento ---")
print('Quem pode utilizar este serviço?\n'
      '--- É obrigatório para homens ---'
      '- Jovem brasileiro do sexo masculino no ano em que completar 18 anos.\n'
      '- Brasileiro Naturalizado ou por opção.\n'
      '- Qualquer cidadão que não tenha se alistado no ano em que completou 18 anos.'
      )
sexo = int(input('Qual o seu sexo: [1] Masculino [2] Feminino: '))
anoNascimento = int(input('Em qual ano você nasceu? '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
alistamento = abs(idade - 18)

if sexo == masculino:
    if anoNascimento >= 1900:
        if idade < 18:
            anoAlistamento = anoAtual + alistamento
            print(
                f"Você nasceu em {anoNascimento} e fará {idade} anos. Faltam {alistamento} anos para se alistar no serviço militar.")
            print(f"Seu alistamento será em {anoAlistamento}.")
        elif idade > 18:
            anoAlistamento = anoAtual - alistamento
            if alistamento == 1:
                print(
                    f"Você nasceu em {anoNascimento} e fará {idade} anos. Passou {alistamento} ano para se alistar no serviço militar.")
                print(f"Seu alistamento foi em {anoAlistamento}.")
            else:
                print(
                    f"Você nasceu em {anoNascimento} e fará {idade} anos. Passou {alistamento} anos para se alistar no serviço militar.")
                print(f"Seu alistamento foi em {anoAlistamento}.")
        else:
            print(
                f"Você nasceu em {anoNascimento} e fará {idade} anos. Chegou a hora de se alistar no serviço militar.")
    else:
        print(f"O ano em que você nasceu é inferior a 1900!")
elif sexo == feminino:
    print(f"No alistamento militar no Brasil é obrigatório apenas para homens. "
          f"No entanto, as mulheres podem ingressar voluntariamente nas Forças Armadas por meio de concursos específicos.")
else:
    print('O valor digitado para sexo é inválido!')