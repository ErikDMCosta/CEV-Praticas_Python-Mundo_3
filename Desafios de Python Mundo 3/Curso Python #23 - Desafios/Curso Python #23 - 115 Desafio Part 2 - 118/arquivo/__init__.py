from interface import *

def ArquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')

def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        print(a.read())
