num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # NÃO É POSSIVEL ADCIONAR VALORES DESSA MANEIRA
num.append(7) # ASSIM È A MENEIRA CORRETA
num.sort() # IRÁ POR EM ORDEM A LISTA
print(num)
print(f'Esta LISTA tem {len(num)} elementos.') # len FAZ LEITURA DE QUANTOS ELEMENTOS POSSUÍ NA LISTA
