lista = []
pergunta = 'S'
while pergunta == "S":
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
