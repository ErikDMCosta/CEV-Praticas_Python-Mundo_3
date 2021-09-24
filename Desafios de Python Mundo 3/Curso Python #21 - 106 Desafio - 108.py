from time import sleep
resp = str
while True:
    print('\033[m\033[42m~' * 30)
    print('   SISTEMA DE AJUDA PyHELP')
    print('~' * 30)
    resp = str(input('\033[mFunção ou Biblioteca > ')).lower()
    if resp == 'fim':
        print('\033[m\033[41m~' * 15)
        print('   ATÉ LOGO!')
        print('~' * 15)
        break
    print('\033[44m~' * 51)
    print(f"        Acessando o manual do comando '{resp}'")
    print('~' * 51)
    sleep(1.5)
    print('\033[07;40m')
    help(resp)
    sleep(2.5)
