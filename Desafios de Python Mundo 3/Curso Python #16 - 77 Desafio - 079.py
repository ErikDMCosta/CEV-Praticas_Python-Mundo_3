palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro',)
for sequencia in range(0, len(palavras)):
    print('\nNa palavra {} temos '.format((palavras[sequencia]).upper()), end='')
    for contador in range(0, len(palavras[sequencia])):
        if palavras[sequencia][contador] == 'a':
            print(' a ', end='')
        elif palavras[sequencia][contador] == 'e':
            print(' e ', end='')
        elif palavras[sequencia][contador] == 'i':
            print(' i ', end='')
        elif palavras[sequencia][contador] == 'o':
            print(' o ', end='')
        elif palavras[sequencia][contador] == 'u':
            print(' u ', end='')
