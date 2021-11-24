expressao = str(input('Digite a expressão: '))
cont1 = cont2 = str
lista = []
for i in expressao:
    cont1 = expressao.count('(')
    cont2 = expressao.count(')')
    lista.append(i)
if cont1 == cont2:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
