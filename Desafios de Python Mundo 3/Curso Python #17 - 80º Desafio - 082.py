valores = []
for contador in range(0, 5):
    valor = int(input('Digite um valor: '))
    if contador == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
