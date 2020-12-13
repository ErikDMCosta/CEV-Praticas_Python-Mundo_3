num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # NÃO É POSSIVEL ADCIONAR VALORES DESSA MANEIRA
num.append(7) # ASSIM È A MENEIRA CORRETA
num.sort(reverse=True) # IRÁ POR EM ORDEM REVERSA A LISTA
num.insert(2, 2) # NA POSIÇÃO 2 INSERIR O VALOR 2
num.remove(2) # REMOVE ELEMENTO 2 NA PRIMEIRA OCORRÊCIA VIZUALIZADA
print(num)
print(f'Esta LISTA tem {len(num)} elementos.') # len FAZ LEITURA DE QUANTOS ELEMENTOS POSSUÍ NA LISTA
