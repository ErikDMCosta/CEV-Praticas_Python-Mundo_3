from random import randint
escolhidos = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for numeros in escolhidos:
    print(f'{numeros}', end=' ')
print(f'\nO maior valor sorteado foi {max(escolhidos)}')# Método que funciona em Tuplas e outros lugares (mostra maior)
print(f'O menor valor sorteado foi {min(escolhidos)}')# Método que funciona em Tuplas e outros lugares (mostra menor)
