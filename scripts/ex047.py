# Recebe três comprimentos e determina se pode ser um triângulo e o seu tipo.

a = float(input('Digite o valor da primeiro segmento: '))
b = float(input('Digite o valor da segundo segmento: '))
c = float(input('Digite o valor da terceiro segmento: '))


if (a + b > c) and (a + c > b) and (b + c > a):
    print('\033[32mOs segmentos acima podem formar um triângulo ', end='')
    if a == b == c:
        print('equilátero!\033[m')
    elif a != b != c != a:
        print('escaleno!\033[m')
    else:
        print('isósceles!\033[m')
else:
    print('\033[31mOs segmentos acima não podem formar um triângulo!\033[m')