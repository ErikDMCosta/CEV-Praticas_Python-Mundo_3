from time import sleep

def linha(tam=40):
    return '-' * tam

def cabecalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def Op1():
    print(linha())
    print('Opção 1'.center(40))
    print(linha())
    Menu()

def Op2():
    print(linha())
    print('Opção 2'.center(40))
    print(linha())
    Menu()

def Menu():
    print(linha())
    print('Menu Principal'.center(40))
    print(linha())
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print(linha())
    while True:
        escolha = int(input('\033[32mSua Opção: \033[m'))
        if escolha == 1:
            sleep(1)
            Op1()
        elif escolha == 2:
            sleep(1)
            Op2()
        elif escolha == 3:
            sleep(1)
            print(linha())
            print('Saindo do sistema... Até logo!'.center(40))
            print(linha())
            break
        else:
            sleep(1)
            print('\033[31mERRO! Digite uma opção válida!\033[m')
