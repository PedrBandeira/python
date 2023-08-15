# Este código interage com o usuário para obter a quantidade de quilômetros percorridos por um carro alugado e o número de dias de aluguel. Com essas informações, é realizado um cálculo preciso do valor a ser pago, levando em consideração uma taxa diária de R$60 e um adicional de R$0,15 por quilômetro rodado. O resultado final exibe o montante a ser pago pelo aluguel do carro, considerando tanto as diárias quanto a distância percorrida.

# Declaração das variáveis
diasAlugado = int(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos Km rodados? '))
diaria = 60
custoPorKm = 0.15

# Realiza o cálculo do total a pagar
valorDiarias = diasAlugado * diaria
valorKm = custoPorKm * kmRodados
valor = valorDiarias + valorKm

# Exibe o resultado
print(f"Quantidade de dias alugados: {diasAlugado} dias")
print(f"Quantidade de Km rodados: {kmRodados}Km")
print(f"Valor total das diárias: R${valorDiarias:.2f}")
print(f"Valor dos Km rodados: R${valorKm:.2f}")
print(f"O total a pagar é de R${valor:.2f}")