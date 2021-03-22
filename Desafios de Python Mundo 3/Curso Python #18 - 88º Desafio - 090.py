from random import randint
from time import sleep
print('-' * 43)
print('            JOGO NA MEGA SENA')
print('-' * 43)
lista = list()
jogos = list()
count = 0
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-=-= SORTEANDO {pergunta} JOGOS =-=-=-=-=-=-')
while count < pergunta:
    aux = 0
    while True:
        randomico = randint(1, 60)
        if randomico not in lista:
            lista.append(randomico)
            aux += 1
        if aux >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    count += 1
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
