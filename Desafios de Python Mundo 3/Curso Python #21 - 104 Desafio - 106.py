def leiaInt():
    print('-' * 30)
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            return f'Você acabou de digitar o número {n}'
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

print(leiaInt())
