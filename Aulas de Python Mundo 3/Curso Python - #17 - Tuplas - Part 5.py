num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # NÃO É POSSIVEL ADCIONAR VALORES DESSA MANEIRA
num.append(7) # ASSIM È A MENEIRA CORRETA
num.sort(reverse=True) # IRÁ POR EM ORDEM REVERSA A LISTA
num.insert(2, 0) # INSERINDO VALORES A PARTIR DAS POSIÇÕES DA LISTA
num.pop() # IRÁ REMOVER O ÚLTIMO ELEMENTO NO CASO VALOR 1
num.pop(2) # IRÁ REMOVER O ÚLTIMO ELEMENTO do ÍNDICE 2 COM VALOR 0
print(num)
print(f'Esta LISTA tem {len(num)} elementos.') # len FAZ LEITURA DE QUANTOS ELEMENTOS POSSUÍ NA LISTA
