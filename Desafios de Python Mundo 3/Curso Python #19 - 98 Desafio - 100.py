from time import sleep

def linha():
    print('-=' * 15)

def contagem():
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    sleep(2.5)
    for contando in range(1, 11, 1):
        print(contando, end=' ', flush=True)
        sleep(0.3)
    print('FIM!')
    linha()
    print('Contagem de 10 até 0 de 2 em 2')
    sleep(2)
    for contando in range(10, -1, -2):
        print(contando, end=' ', flush=True)
        sleep(0.3)
    print('FIM!')
    linha()

def contador():
    contagem()
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    if (inicio <= fim) and (passo >= 1):
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for Contador in range(inicio, fim, passo):
            print(Contador, end=' ', flush=True)
            sleep(0.6)
        print('FIM!')
    elif (inicio >= fim) and (passo >= 1):
        print(f'Contagem de {fim} até {inicio} de {passo} em {passo}')
        fim -= passo
        for Contador in range(inicio, fim, -passo):
            if fim <= inicio:
                print(Contador, end=' ', flush=True)
                sleep(0.6)
        print('FIM!')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        fim += passo
        for Contador in range(inicio, fim, +passo):
            if fim <= inicio:
                print(Contador, end=' ', flush=True)
                sleep(0.6)
        print('FIM!')
contador()
