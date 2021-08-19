from time import sleep

def maior(* numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    pos = 0
    aux = 0
    valores = 0
    while pos < len(numeros):
        if numeros[0] == 0:
            valores = (len(numeros) - 1)
            break
        elif numeros[pos] >= aux:
            aux = numeros[pos]
            valores = len(numeros)
        print(numeros[pos], end=' ', flush=True)
        sleep(0.3)
        pos += 1
    print(f'Foram informados {valores} valores ao todo.')
    print(f'O maior valor informado foi {aux}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
