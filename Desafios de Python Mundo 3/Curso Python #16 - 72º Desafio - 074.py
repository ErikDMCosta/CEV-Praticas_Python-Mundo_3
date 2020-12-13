extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    digito = int(input('Digite um número de 0 e 20: '))
    if digito < 0 or digito > 20:
        digito = int(input('Tente novamente. Digite um número de 0 e 20: '))
    else:
        break
print(f'Voce digitou o número {extenso[digito]}')
