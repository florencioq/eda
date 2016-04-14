from Lista01.Q04ListaEncadeadaOrdenadaCircular import *

print("1) Criar uma lista vazia")
listaEncadeadaOrdenadaCircular = ListaEncadeadaOrdenadaCircular()

print("5) Verificar se a lista esta vazia")
print(listaEncadeadaOrdenadaCircular.esta_vazia())

print("2) Inserir elementos no início da lista")
for n in range(20):
    listaEncadeadaOrdenadaCircular.inserirOrdenado(random.randint(-5, 5))
    listaEncadeadaOrdenadaCircular.printLista()

print("3) Imprimir elementos de uma lista encadeada")
listaEncadeadaOrdenadaCircular.printLista()

print("4.2) Imprimir elementos recursivamente versão 2")
listaEncadeadaOrdenadaCircular.printListaRecursivo()
print(" ")

print("5) Verificar se a lista está vazia")
print(listaEncadeadaOrdenadaCircular.esta_vazia())

print("7) Buscar recuperar um elemento da lista")
for i in range(10):
    print(listaEncadeadaOrdenadaCircular.buscaElemento(i))

print("8) Apagar alguns itens")
print("8.1 Listando os elementos antes")
listaEncadeadaOrdenadaCircular.printLista()

print("8.2 Removendo os elementos 15 (não existente), -5 (primeiro), 5 (último) e o -2 (intermediário)")
listaEncadeadaOrdenadaCircular.removeItem(15)  ## esse não existe
listaEncadeadaOrdenadaCircular.removeItem(-5)
listaEncadeadaOrdenadaCircular.removeItem(5)
listaEncadeadaOrdenadaCircular.removeItem(-2)

print("8.3 Listando os elementos depois")
listaEncadeadaOrdenadaCircular.printLista()

print("9) Remove com recursão (-4, 0, 4 e 6 (inexistente))")
listaEncadeadaOrdenadaCircular.removeItemRecursivamente(-4)
listaEncadeadaOrdenadaCircular.printLista()
listaEncadeadaOrdenadaCircular.removeItemRecursivamente(0)
listaEncadeadaOrdenadaCircular.printLista()
listaEncadeadaOrdenadaCircular.removeItemRecursivamente(4)
listaEncadeadaOrdenadaCircular.printLista()
listaEncadeadaOrdenadaCircular.removeItemRecursivamente(6)
listaEncadeadaOrdenadaCircular.printLista()

print("10) Libera a memória")
listaEncadeadaOrdenadaCircular.libera()