# Este código solicita ao usuário que insira um número e, em seguida, gera e imprime na tela a tabuada desse número, indo de 1 até 10. Cada linha da tabuada mostra a multiplicação do número escolhido pelo contador correspondente, formatada de maneira alinhada e legível.

# Solicita a entrada de um valor para a tabuada
num = int(input('Digite um número para ver sua tabuada: '))

# Linha de separação
print(f"-"*15) 

# Declaração do contador (i) e execução do loop while
i = 1
while i <= 10:
    resultado = num * i
    print(f"{num} x {i:2} = {resultado:3}")
    i += 1

# Linha de separação
print(f"-"*15) 