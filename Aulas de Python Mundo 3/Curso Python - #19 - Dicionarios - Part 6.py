estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado[])
    # brasil.append(estado[:])
    brasil.append(estado.copy())
for e in brasil:
    print(e)
    print()
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.items():
        print(v, end=' ')
    print()
