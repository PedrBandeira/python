# O programa determina a partir da idade do usuário em qual categoria ele se encaixa:
# mirim (<9), infantil (<14), junior (<19), senior (<20) e master (>20)

from datetime import date

print('--- Confederação Nacional de Natação ---')
anoNascimento = int(input('Em qual ano você nasceu? '))
idade = date.today().year - anoNascimento

if 0 <= idade <= 9:
    print(f"Você têm (ou fará) {idade} anos. E se encaixa na categoria MIRIM")
elif idade <= 14:
    print(f"Você têm (ou fará) {idade} anos. E se encaixa na categoria INFANTIL")
elif idade <= 19:
    print(f"Você têm (ou fará) {idade} anos. E se encaixa na categoria JÚNIOR")
elif idade <= 20:
    print(f"Você têm (ou fará) {idade} anos. E se encaixa na categoria SÊNIOR")
else:
    print(f"Você têm (ou fará) {idade} anos. E se encaixa na categoria MASTER")