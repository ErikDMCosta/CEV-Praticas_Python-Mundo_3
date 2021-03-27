dados = dict()
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif 7 < dados['média'] <= 5:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-=' * 30)
for keys, values in dados.items():
    print(f'  - {keys} é igual a {values}')
