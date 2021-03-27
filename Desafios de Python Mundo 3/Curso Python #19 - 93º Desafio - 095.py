partidas = list()
jogadas = dict()
soma = 0
vezes = 0
jogadas['nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {jogadas["nome"]} jogou? '))
for partida in range(0, jogos):
    partidas.append(int(input(f'Quantos gols na partida {partida}? ')))
    soma += partidas[-1]
    vezes += 1
jogadas['gols'] = partidas[:]
jogadas['total'] = soma
print('-=' * 30)
print(jogadas)
print('-=' * 30)
for keys, values in jogadas.items():
    print(f'O campo {keys} tem o valor {values}')
print('-=' * 30)
print(f'O jogador {jogadas["nome"]} jogou {vezes} partidas.')
for indice, lista in enumerate(partidas):
    print(f'    => Na partida {indice}, fez {lista} gols.')
print(f'Foi um total de {soma} gols.')
