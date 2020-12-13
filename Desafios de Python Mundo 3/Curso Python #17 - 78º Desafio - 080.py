valores = []
maior = menor = limite = 0

while limite < 5:
    valores.append(int(input(f'Digite um valor para a Posição {limite}: ')))
    if limite == 0:
        maior = menor = valores[limite]
    else:
        if valores[limite] > maior:
            maior = valores[limite]
        if valores[limite] < menor:
            menor = valores[limite]
    limite += 1
print('-=' * 40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}º, ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}º, ', end='')
