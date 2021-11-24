dados = [[], []]
guardado = int
for count in range(0, 7):
    guardado = int(input(f'Digite {count + 1}º. Valor: '))
    if guardado % 2 == 0:
        dados[0].append(guardado)
    else:
        dados[1].append(guardado)
print('-=' * 30)
print(f'Os valores pares digitados foram: {dados[0]}')
print(f'Os valores ímpares digitados foram: {dados[1]}')
