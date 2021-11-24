teste = list()
teste.append("Erik")
teste.append(21)
# print(teste)
galera = list()
# galera.append(teste)
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
# galera.append(teste)
galera.append(teste[:])
print(galera)
