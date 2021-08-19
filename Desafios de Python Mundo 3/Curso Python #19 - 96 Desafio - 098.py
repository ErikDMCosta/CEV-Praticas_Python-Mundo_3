def area():
    print('Controle de Terrenos')
    print('-' * 30)
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    resultado = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {resultado}m².')

area()
