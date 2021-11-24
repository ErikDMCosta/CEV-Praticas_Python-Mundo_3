pessoas = {'nome': 'Erik', 'sexo': 'M', 'idade': 21}
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
