from Q1 import *

myHeap = Heap()
myHeap.printHeap()

## Inserindo itens
print("Inserindo elementos")
print("-------------------")
for i in range(10, 0, -1):
    myHeap.add(randint(1, 100), randint(1, 100))
    myHeap.printHeap()
    print("------------------")
## Removendo pela cabeça
print("Removendo elementos pela cabeça")
print("-------------------")
for i in range(1):
    myHeap.remove_minimo()
    myHeap.printHeap()
    print("------------------")
print("Recuperando alguns elementos pela Chave")
for i in range(50):
    e = myHeap.recupera_linear(i)
    if e != None:
        print(e._chave, e._valor)
## Incluindo e removendo itens aleatoriamente
print("Inserindo,recuperando e removendo elementos")
print("-------------------------------")
for i in range(5):
    elemento = myHeap.add(randint(1, 100), randint(1, 100))
    print("Inserindo Elemento: " + str(elemento._chave))
    myHeap.printHeap()
    print("------------------")
    print("Removendo Elemento: " + str(elemento._chave))
    myHeap.remove(elemento)
    myHeap.printHeap()
    print("------------------")
print("Liberando memória")
myHeap.libera()
del myHeap
