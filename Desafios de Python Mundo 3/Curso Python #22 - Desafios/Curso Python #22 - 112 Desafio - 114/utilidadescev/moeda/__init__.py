def aumentar(num=0, porc=0, formato=False):
    """
    -> Aumenta um valor em uma dada porcentagem.

    Parâmetros opcionais
    :param num: Valor monetário
    :param porc: Número da porcentagem
    :param formato: Booleano que indica se a formatação será feita
    :return:
    """
    resultado = num + (num * (porc / 100))
    return resultado if formato is False else moeda(resultado)

def diminuir(num=0, porc=0, formato=False):
    """
    -> Diminui um valor em uma dada porcentagem.

    Parâmetros opcionais
    :param num: Valor monetário
    :param porc: Número da porcentagem
    :param formato: Booleano que indica se a formatação será feita
    :return:
    """
    resultado = num - (num * porc / 100)
    return resultado if formato is False else moeda(resultado)

def dobro(num=0, formato=False):
    """
    -> Dá o dobro de um valor.

    Parâmetros opcionais
    :param num: Valor monetário
    :param formato: Booleano que indica se a formatação será feita
    :return:
    """
    resultado = num * 2
    return resultado if not formato else moeda(resultado)

def metade(num=0, formato=False):
    """
    -> Dá a metade de um valor.

    Parâmetros opcionais
    :param num: Valor monetário
    :param formato: Booleano que indica se a formatação será feita
    :return:
    """
    resultado = num / 2
    return resultado if not formato else moeda(resultado)

def moeda(preco=0, moeda='R$'):
    """
    -> Formata um dado valor monetário.

    Parâmetros opcionais
    :param preco: Valor que será formatado.
    :param moeda: Símbolo da Moeda.
    :return:
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
