# PECULIARIDADE DO PYTHON
a = [2, 3, 4, 7]
b = a[:] # COPIANDO LISTAS
# b RECEBE UMA COPIA DE TODOS OS VALORES DE a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
