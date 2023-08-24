# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(f'-' * 40)
print('Usando for in lanche:')
print(f'-' * 40)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'-' * 40)
print('Usando for in lanche com posição:')
print(f'-' * 40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(f'-' * 40)
print(f"{'OU': ^40}")
print(f'-' * 40)

print('Usando for in range(0, length(lanche)')
print(f'-' * 40)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print(f'-' * 40)

print('Comi para caramba!')