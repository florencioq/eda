from Q2 import *

b = int(input("Entre com o tamanho de cada bucket: "))

# A Hash terá a metade do numero de chaves
myHashTable = HashTable(int(b))

print("=========================")
print("Incluindo alguns elementos")
print("=========================")
elem = [24, 248, 152, 136, 232, 120, 41, 185, 43, 107]
for i in elem:
    myHashTable.setitem(i, i)
    myHashTable.print()
