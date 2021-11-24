pessoas = {'nome': 'Erik', 'sexo': 'M', 'idade': 21}
for k in pessoas.keys():
    print(k)
print('-=' * 10)
for k in pessoas.values():
    print(k)
print('-=' * 10)
for k, v in pessoas.items():
    print(f'{k} = {v}')
