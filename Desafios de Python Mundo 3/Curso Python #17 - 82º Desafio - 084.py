lista = []
par = []
impar = []
pergunta = 'S'
while pergunta == "S":
    valor = int(input('Digite um número: '))
    lista.append(valor)
    if valor % 2 == 0:  # PAR
        par.append(valor)
    else:  # IMPAR
        impar.append(valor)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
