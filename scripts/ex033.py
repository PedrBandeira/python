# O programa lê a velocidade de um carro. Se ele ultrapassar 80km/h, ele foi multado.
# A multa custa R$7 por cada km acima do limite.

velocidade = float(input('Qual a velocidade do carro? '))
limite = 80
multa = 7

if velocidade > limite:
    valorMulta = (velocidade - limite) * multa
    print(f"O seu carro estava a {velocidade - limite}km/h acima do limite de 80km/h.")
    print(f"Você foi multado em R${valorMulta}!")
else:
    print(f"Parabéns, seu carro está a {velocidade}km/h e está sob os limites de velocidade.")