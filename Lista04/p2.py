from Q2 import *

b = int(input("Entre com o tamanho de cada bucket: "))

# A Hash terá a metade do numero de chaves
myHashTable = HashTable(int(b))

print("=========================")
print("Incluindo alguns elementos")
print("=========================")
for i in range(1, 10):
    myHashTable.setitem(i, randint(1, 1000))
    myHashTable.print()

print("=========================")
print("Excluindo alguns elementos")
print("=========================")
for i in range(1, 10, 3):
    myHashTable.delitem(i)
    myHashTable.print()

print("=========================")
print("Buscando alguns elementos")
print("=========================")
for i in range(1, 11):
    retorno = myHashTable.getitem(i)
    if retorno != None:
        print(str(i) + "-" + str(retorno))

print("=========================")
print("Liberando a memória")
print("=========================")
myHashTable.libera()

del myHashTable
