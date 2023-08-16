# O programa lê a velocidade de um carro. Se ele ultrapassar 80km/h, ele foi multado.
# A multa custa R$7 por cada km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro? '))
limite = 80
multa = 7

if velocidade > limite:
    valorMulta = (velocidade - limite) * multa
    print(f"O seu carro estava a {velocidade - limite:.2f}km/h acima do limite de 80km/h.")
    print(f"Você foi multado em R${valorMulta:.2f}!")
else:
    print(f"Parabéns, seu carro está a {velocidade:.2f}km/h e está sob os limites de velocidade.")

print('Tenha um bom dia e dirija com segurança!')
