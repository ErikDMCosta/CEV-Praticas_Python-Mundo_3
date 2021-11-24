from arquivo import *
from time import sleep

def linha(tam=40):
    return '-' * tam

def cabecalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def Op1(arquivo):
    # Opção de listar o conteúdo de um arquivo de texto
    print(linha())
#   print('Opção 1'.center(40))
    cabecalho('PESSOAS CADASTRADAS')
    lerArquivo(arquivo)
    print(linha())
    Menu()

def Op2(arquivo):
    print(linha())
    print('Opção 2'.center(40))
    print(linha())
    Menu()

def Menu():
    arquivo = 'Cadastros.txt'
    """
    if ArquivoExiste(arquivo):
        print('Arquivo encontrado com sucesso!'.center(40))
    else:
        print('Arquivo não encontrado!'.center(40))
        criarArquivo(arquivo)
    """
    if not ArquivoExiste(arquivo):
        criarArquivo(arquivo)

    print(linha())
    print('Menu Principal'.center(40))
    print(linha())
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print(linha())
    while True:
        escolha = int(input('\033[32mSua Opção: \033[m'))
        """try:"""
        if escolha == 1:
            sleep(1)
            Op1(arquivo)
        elif escolha == 2:
            sleep(1)
            Op2(arquivo)
        elif escolha == 3:
            sleep(1)
            print(linha())
            print('Saindo do sistema... Até logo!'.center(40))
            print(linha())
            break
        else:
            sleep(1)
            print('\033[31mERRO! Digite uma opção válida!\033[m')
"""
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mPrograma interrompido pelo usúario.\033[m')
            break
"""
