from Lista01.Q05ListaDuplamenteEncadeadaOrdenadaCircular import *

print("1) Criar uma lista vazia")
listaDuplamenteEncadeadaOrdenadaCircular = ListaDuplamenteEncadeadaOrdenadaCircular()

print("5) Verificar se a lista esta vazia")
print(listaDuplamenteEncadeadaOrdenadaCircular.esta_vazia())

print("2) Inserir elementos no início da lista")
for n in range(10):
    listaDuplamenteEncadeadaOrdenadaCircular.inserirOrdenado(random.randint(-5, 5))
    listaDuplamenteEncadeadaOrdenadaCircular.printLista()
    listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

print("3) Imprimir elementos de uma lista encadeada")
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

print("4.2) Imprimir elementos recursivamente versão 2")
listaDuplamenteEncadeadaOrdenadaCircular.printListaRecursivo()
print(" ")
print("4.3 Listando normal pra acompanhar")
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

print("5) Verificar se a lista está vazia")
print(listaDuplamenteEncadeadaOrdenadaCircular.esta_vazia())

print("7) Buscar recuperar um elemento da lista")
for i in range(10):
    print(listaDuplamenteEncadeadaOrdenadaCircular.buscaElemento(i))

print("8) Apagar alguns itens")
print("8.1 Listando os elementos antes")
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

print("8.2 Removendo os elementos 15 (não existente), -5 (primeiro), 5 (último) e o -2 (intermediário)")
listaDuplamenteEncadeadaOrdenadaCircular.removeItem(15)  ## esse não existe
listaDuplamenteEncadeadaOrdenadaCircular.removeItem(-5)
listaDuplamenteEncadeadaOrdenadaCircular.removeItem(5)
listaDuplamenteEncadeadaOrdenadaCircular.removeItem(-2)

print("8.3 Listando os elementos depois")
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

print("9) Remove com recursão (-4, 0, 4 e 6 (inexistente))")
listaDuplamenteEncadeadaOrdenadaCircular.removeItemRecursivamente(-4)
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

listaDuplamenteEncadeadaOrdenadaCircular.removeItemRecursivamente(0)
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

listaDuplamenteEncadeadaOrdenadaCircular.removeItemRecursivamente(4)
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

listaDuplamenteEncadeadaOrdenadaCircular.removeItemRecursivamente(6)
listaDuplamenteEncadeadaOrdenadaCircular.printLista()
listaDuplamenteEncadeadaOrdenadaCircular.printListaReverso()

print("10) Libera a memória")
listaDuplamenteEncadeadaOrdenadaCircular.libera()
