from Q1 import *

n = int(input("Entre com o número de chaves: "))

# O bucket terá a metade do numero de chaves
myHashTable = HashTable(int(n / 2))

print("Incluindo alguns elementos")
print("=========================")
for i in range(1, n + 1):
    if not myHashTable.setitem(i, randint(1, 1000)):
        print("Colisão")
    print("-------------------------")
    myHashTable._printHash()
print("=========================")
print("Buscando alguns elementos")
print("=========================")
for i in range(1, n + 1):
    retorno = myHashTable.getitem(i)
    if retorno != None:
        print(str(i) + "-" + str(retorno))
print("=========================")
print("Eliminando alguns elementos")
print("=========================")
for i in range(1, n, 2):
    retorno = myHashTable.remitem(i)
myHashTable._printHash()

print("=========================")
print("Liberando a memória")
print("=========================")
myHashTable.libera()

del myHashTable
