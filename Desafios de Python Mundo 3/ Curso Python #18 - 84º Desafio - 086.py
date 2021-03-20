# Curso Python #18 - Desafio - 084 (Uma solução alternativa) #
dados = list()
pesado = list()
guarda = int
leve = list()
maior = 0
menor = 0
pergunta = 'S'
quantia = 0
while pergunta != 'N':
    dados.append(str(input('Nome: ')))
    quantia += 1
    dados.append(float(input('Peso: ')))
    guarda = dados[-1]
    if dados[-1] >= 80:
        pesado.append(dados[-2])
        if maior == 0:
            maior = guarda
        elif pesado[-1] >= pesado[-2]:
            maior = pesado[-1]
    elif dados[-1] <= 60:
        leve.append(dados[-2])
        if menor == 0:
            menor = guarda
        elif leve[-1] >= leve[-2]:
            menor = leve[-1]
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=' * 25)
print(f'Ao todo, você cadastrou {quantia} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
aux = 1
while aux <= len(pesado):
    print(f'{pesado[aux - 1]}', end=' ')
    aux += 1
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
aux = 1
while aux <= len(leve):
    print(f'{leve[aux - 1]}', end=' ')
    aux += 1
