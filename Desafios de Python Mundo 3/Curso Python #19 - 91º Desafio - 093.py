from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for keys, values in jogadas.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for keys, values in enumerate(ranking):
    print(f'   {keys + 1}º lugar: {values[0]} com {values[1]}.')
    sleep(1)
