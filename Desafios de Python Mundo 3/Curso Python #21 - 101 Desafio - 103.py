def voto(anoNascimento):
    import datetime
    anoAtual = datetime.date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade > 65 or 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

pergunta = voto(int(input('Em que ano você nasceu? ')))
print(pergunta)
