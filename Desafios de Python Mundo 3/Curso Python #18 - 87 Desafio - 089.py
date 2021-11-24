dados = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somaterceira = 0
maiorterceira = 0
for x in range(0, 3):
    for y in range(0, 3):
        dados[x][y] = int(input(f'Digite um valor para [{x}],[{y}]: '))
        if dados[x][y] % 2 == 0:
            somapar += dados[x][y]
        if maiorterceira == 0 and y == 2:
            maiorterceira = dados[x][y]
        if y == 2:
            somaterceira += dados[x][y]
            if maiorterceira < dados[x][y]:
                maiorterceira = dados[x][y]
print('-=' * 30)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{dados[x][y]:^5}]', end='')
    print('')
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maiorterceira}.')
