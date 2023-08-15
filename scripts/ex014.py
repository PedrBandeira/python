# Este código permite ao usuário fornecer um valor em metros. Em seguida, realiza conversões desse valor para outras unidades do sistema métrico decimal, incluindo quilômetros, hectômetros, decâmetros, decímetros, centímetros, milímetros, pés e polegadas. Os resultados das conversões são exibidos de forma formatada, permitindo ao usuário visualizar facilmente a equivalência entre o valor em metros e suas correspondentes unidades de medida. O uso de constantes para os fatores de conversão e comentários explicativos contribui para a clareza e legibilidade do código.

# Solicita a entrada do valor em metros
metros = float(input('Digite o valor em metros: '))

# Realiza as conversões
quilometros = metros * 0.001
hectometros = metros * 0.01
decametros = metros * 0.1
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000
pes = metros * 3.28084
polegadas = metros * 39.3701

# Exibe os resultados formatados
print(f"A medida de {metros}m corresponde à:")
print(f"{quilometros:.3f}km")
print(f"{hectometros:.2f}hm")
print(f"{decametros:.1f}dam")
print(f"{decimetros:.0f}dm")
print(f"{centimetros:.0f}cm")
print(f"{milimetros:.0f}mm")
print(f"{pes}ft")
print(f"{polegadas}in")