lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita')
#lanche recebe 0      ,    1  ,    2   ,    3   ,        4

for comida in lanche:
    print(f'Eu vou comer {comida}') # Neste aqui não tem como mostrar a posição
print()

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # Neste aqui irá mostrar a posição

print('\nComi pra caramba!')
