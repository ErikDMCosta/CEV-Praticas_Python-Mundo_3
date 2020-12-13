times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*56)
print(f'Lista de times do Brasileirão: {times}')

print('-='*56)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*56)
print(f'Os 4 últimos são {times[16:20]}')
print('-='*56)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*56)
print(f'O {times[7]} está na {times.index("Chapecoense") + 1}º posição.')
