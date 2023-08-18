# O Programa mostra uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 a 0, com pausa de 1 segundo entre eles
from time import sleep
print('--- Contagem Regressiva ---')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('--- 🎉🎉🎉 ---')
