listagem = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)

material = 0
preco = 1

print('-' * 46)
print((' ' * 14) + 'LISTAGEM DE PREÇOS')
print('-' * 46)

for contador in listagem:

    if type(contador) is str:
        print(f'{contador:.<37}', end='')

    else:
        print(f'R${contador:>7.2f}')
print('-' * 46)

'''
OU TAMBÉM PODE SER:

while True:
    if material <= 18 and preco <= 17:
        print(f'{listagem[material]:.<}', end='')
        if len(listagem[material]) == 5:
            print('.' * 32, end='')
        elif len(listagem[material]) == 6:
            print('.' * 31, end='')
        elif len(listagem[material]) == 7:
            print('.' * 30, end='')
        elif len(listagem[material]) == 8:
            print('.' * 29, end='')
        elif len(listagem[material]) == 12:
            print('.' * 25, end='')

        print(f' R$ {listagem[preco]:>7.2f}')
        material += 2
        preco += 2
    else:
        break
print('-' * 46)

'''
