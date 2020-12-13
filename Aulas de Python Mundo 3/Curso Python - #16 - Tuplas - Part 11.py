a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b
cc = b + a

print('Letra A: {}'.format(a))
print('Letra B: {}'.format(b))
print('Concatenação: {}'.format(c))
print('Concatenação invertida: {}'.format(cc))
print('Tamanho da tupla C é {} elementos.'.format(len(cc)))
print('O número cinco se repete dentro da tupla C é de {} vezes.'.format(cc.count(5)))
print('O número quatro se repete dentro da tupla C é de {} vezes.'.format(cc.count(4)))
print('O número nove se repete dentro da tupla C é de {} vezes.'.format(cc.count(9)))
print('O número oito está {}º posição.'.format(cc.index(8)))
print('O número quatro está {}º posição.'.format(cc.index(4)))
print('O número dois está {}º posição.'.format(cc.index(2)))
print('O número dois está {}º posição começando da posição quatro.'.format(cc.index(2, 4)))
print('O número cinco está {}º posição começando da posição um.'.format(cc.index(5, 1))) # cc.index(5, 1) - Chamamos isso de deslocamento
