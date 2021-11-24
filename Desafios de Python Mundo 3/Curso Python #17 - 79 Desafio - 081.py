valores = []
resposta = str
digito = int
while True:
    digito = int(input('Digite um valor: '))
    if digito not in valores:
        valores.append(digito)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adcionar...')
    resposta = str(input('Quer continuar? [S/N] ').upper().strip('IM' or 'ÃO' or 'AO'))
    if resposta == 'N':
        break
    valores.sort()
print('-=' * 30)
print(f'Você digitou os valores {valores}')
