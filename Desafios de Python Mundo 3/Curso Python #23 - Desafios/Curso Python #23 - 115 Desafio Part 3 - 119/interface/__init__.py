from arquivo import *
from time import sleep
import sys

def linha(tam=40):
    return '-' * tam

def cabecalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def Op1(arquivo):
    print(linha())
    cabecalho('PESSOAS CADASTRADAS')
    lerArquivo(arquivo)
    print(linha())
    MenuPrincipal()

def Op2(arquivo):
    print(linha())
    # print('Opção 2'.center(40))
    cabecalho('NOVO CADASTRO')
    print(linha())
    nome = str(input('Nome: '))
    idade = str(input('Idade: '))
    cadastrar(arquivo, nome, idade)
    print(linha())
    MenuPrincipal()

def MenuPrincipal():
    arquivo = 'Cadastros.txt'
    if not ArquivoExiste(arquivo):
        criarArquivo(arquivo)

    print(linha())
    print('Menu Principal'.center(40))
    print(linha())
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print(linha())
    try:
        escolha = 0
        while escolha != '3':
            escolha = str(input('\033[32mSua Opção: \033[m'))
            if escolha == '1' or escolha == '2':
                if escolha == '1':
                    sleep(1)
                    Op1(arquivo)
                else:
                    sleep(1)
                    Op2(arquivo)
            elif escolha == '3':
                break
            else:
                sleep(1)
                print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)

    except (ValueError, TypeError):
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

    except KeyboardInterrupt:
        print('\033[31mPrograma interrompido pelo usúario.\033[m')
    else:
        print(linha())
        print('Saindo do sistema... Até logo!'.center(40))
        print(linha())
        sys.exit()
