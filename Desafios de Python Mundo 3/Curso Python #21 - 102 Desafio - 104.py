def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    contador = n
    resultado = guardado = 0
    print('-' * 35)
    while contador >= 0:
        guardado = n * (n - 1)
        resultado += guardado
        contador -= 1
    if show:
        for contando in range(n, 0, -1):
            print(contando, end='')
            if contando > 1:
                print(' x ', end='')
        print(' = ', end='')
    return resultado

print(fatorial(5, show=True))
# help(fatorial)
