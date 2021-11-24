def metade(num=0):
    resultado = num / 2
    return resultado

def dobro(num=0):
    resultado = num * 2
    return resultado

def aumentar(num=0, porc=0):
    resultado = num + (num * porc / 100)
    return resultado

def diminuir(num=0, porc=0):
    resultado = num - (num * porc / 100)
    return resultado

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
