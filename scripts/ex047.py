# Recebe três comprimentos e determina se pode ser um triângulo e o seu tipo.

a = float(input('Digite o valor da primeiro segmento: '))
b = float(input('Digite o valor da segundo segmento: '))
c = float(input('Digite o valor da terceiro segmento: '))


if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) and (a == c):
        print('\033[32mOs segmentos acima podem formar um triângulo equilátero!\033[m')
    elif ((a != b) and (a == c)) or ((b != a) and (b == c)):
        print('\033[32mOs segmentos acima podem formar um triângulo isósceles!\033[m')
    else:
        print('\033[32mOs segmentos acima podem formar um triângulo escaleno!\033[m')
else:
    print('\033[31mOs segmentos acima não podem formar um triângulo!\033[m')