from time import sleep
import random

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = random.randint(1, 10)
        numeros.append(num)
        print(num, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar():
    pos = 0
    soma = 0
    while pos < len(numeros):
        if numeros[pos] % 2 == 0:
            soma += numeros[pos]
        pos += 1
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = []
sorteia()
somaPar()
