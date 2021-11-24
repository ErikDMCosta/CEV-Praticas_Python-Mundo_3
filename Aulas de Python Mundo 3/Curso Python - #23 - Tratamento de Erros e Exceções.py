# print('Oi')
# print(x)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# n = int(input('Número: '))
# print(f'Você digitou o número {n}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente tivemos um problema :(')
# print(f'O resultado é {r}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente tivemos um problema :(')
# else:
#     print(f'O resultado é {r:.1f}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente tivemos um problema :(')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito Obrigado!')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi:( {erro.__class__} ) pela causa:( {erro.__cause__} )')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito Obrigado!')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usúario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi:( {erro.__class__} ) pela causa:( {erro.__cause__} )')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')
