# Lê largura e altura e calcula sua area e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Solicitação das dimensões:
largura = float(input('Digite a largura da área em metros: '))
altura = float(input('Digite a altura da área em metros: '))

# Cálculos:
area = largura * altura
rendimentoTinta = 2 # metros quadrados por litro
quantidadeTinta = area / rendimentoTinta

# Saída Formatada:
print(f"A quantidade de tinta necessária para pintar {area}m\u00b2 é de {quantidadeTinta:.2f} litros.")