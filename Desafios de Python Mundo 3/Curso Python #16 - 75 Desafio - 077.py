digitos = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
nove = 0
contador = 0
tres = 0
parimpar = 0
soma = 0
while contador < 4:
    if digitos[contador] == 9:
        nove += 1
    if digitos[contador] == 3:
        soma = contador + 1
        tres = f'apareceu na {soma}º posição.'
    contador += 1
if soma == 0:
    tres = 'não foi digitado em nenhuma posição.'
print(f'Você digitou os valores {digitos}')
print(f'O valor 9 apareceu {nove} vezes.')
print(f'O valor 3 {tres}')
contador = 0
print(f'Os valores pares digitados foram ', end='')
while contador < 4:
    if digitos[contador] % 2 == 0:
        print(f'{digitos[contador]}', end=' ')
    contador += 1
