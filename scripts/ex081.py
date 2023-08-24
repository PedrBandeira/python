# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre: a) Os 5 primeiros times; b) Os últimos 4 colocados;
# c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Grêmio', 'Athletico-PR', 'Bragantino', 'Fortaleza',
          'Cuiabá', 'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Chapecoense', 'Corinthians', 'Internacional', 'Goias',
          'Bahia', 'Santos', 'Vasco da Gama', 'Coritiba')

print('-='*15)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*15)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*15)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
print('-='*15)
