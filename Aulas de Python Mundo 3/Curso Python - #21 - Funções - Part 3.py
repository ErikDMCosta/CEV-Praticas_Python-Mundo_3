# PARÂMETROS OPCIONAIS
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Érik na aula de Python do CursoemVideo.
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar(b=4, c=2)
somar(c=3, a=2)
somar()

# help(somar)
