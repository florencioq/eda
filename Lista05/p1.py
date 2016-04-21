from Q1 import *

myHeap = Heap()
myHeap.printHeap()
n = 1
## Inserindo itens
print("Inserindo elementos")
print("-------------------")
for i in range(10 * n, 0, -1):
    myHeap.add(randint(1, 100), randint(1, 100))
    myHeap.printHeap()
    print(myHeap.eheap())
    print("------------------")
## Removendo pela cabeça
print("Removendo elementos pela cabeça")
print("-------------------")
for i in range(n):
    myHeap.remove_minimo()
    myHeap.printHeap()
    print(myHeap.eheap())
    print("------------------")
print(myHeap.eheap())
print("Recuperando alguns elementos pela Chave")
for i in range(50):
    e = myHeap.recupera_linear(i)
    if e != None:
        print(e._chave, e._valor)
print(myHeap.eheap())
## Incluindo e removendo itens aleatoriamente
print("Inserindo,recuperando e removendo elementos")
print("-------------------------------")
for i in range(5 * n):
    elemento = myHeap.add(randint(1, 100), randint(1, 100))
    print("Inserindo Elemento: " + str(elemento._chave))
    myHeap.printHeap()
    print(myHeap.eheap())
    print("------------------")
    print("Removendo Elemento: " + str(elemento._chave))
    myHeap.remove(elemento)
    myHeap.printHeap()
    print(myHeap.eheap())
    print("------------------")
print(myHeap.eheap())
print("Alterando elementos")
for i in range(5 * n):
    elemento = myHeap.add(randint(1, 100), randint(1, 100))
    print("Inserindo Elemento: " + str(elemento._chave))
    myHeap.printHeap()
    print(myHeap.eheap())
    print("------------------")
    print("Alterando Elemento: " + str(elemento._chave))
    novachave = randint(1, 100)
    novovalor = randint(1, 100)
    print("Novo Elemento: " + str(novachave))
    myHeap.update(elemento, novachave, novovalor)
    myHeap.printHeap()
    print(myHeap.eheap())
    print("------------------")
print("É um heap?")
print(myHeap.eheap())
print("Liberando memória")
myHeap.libera()
del myHeap