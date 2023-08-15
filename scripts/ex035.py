# Programa pergunta a distância(km) de uma viagem e calcula o preço da passagem
# Sendo R$0,50 por km para viagens de até 200km
# Ou R$0,45 para viagens mais longas

distancia = float(input('Qual a distância em km da viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"A distância da viagem foi de {distancia}km, o valor da passagem é {preco}")
else:
    preco = distancia * 0.45
    print(f"A distância da viagem foi de {distancia}km, o valor da passagem é {preco}")