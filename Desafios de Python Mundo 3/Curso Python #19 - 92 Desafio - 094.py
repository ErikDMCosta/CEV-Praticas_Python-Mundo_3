import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.date.today().year - dados['idade']
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.date.today().year)
print('-=' * 30)
for keys, values in dados.items():
    print(f' - {keys} tem o valor {values}')
