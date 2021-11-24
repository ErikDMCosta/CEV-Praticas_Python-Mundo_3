num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # NÃO É POSSIVEL ADCIONAR VALORES DESSA MANEIRA
num.append(7) # ASSIM È A MENEIRA CORRETA
num.sort(reverse=True) # IRÁ POR EM ORDEM REVERSA A LISTA
num.insert(2, 0) # INSERINDO VALORES A PARTIR DAS POSIÇÕES DA LISTA
print(num)
print(f'Esta LISTA tem {len(num)} elementos.') # len FAZ LEITURA DE QUANTOS ELEMENTOS POSSUÍ NA LISTA
