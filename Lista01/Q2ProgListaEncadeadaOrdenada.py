from Lista01.Q02ListaEncadeadaOrdenada import *

print("1) Criar uma lista vazia")
listaOrdenada = ListaEncadeadaOrdenada()

print("6) Verificar se a lista esta vazia")
print(listaOrdenada.esta_vazia())

print("2) Inserir elementos no início da lista")
for n in range(40):
    listaOrdenada.inserirOrdenado(random.randint(-5, 5))
    listaOrdenada.printLista()

print("3) Imprimir elementos de uma lista encadeada")
listaOrdenada.printLista()

print("4.1) Imprimir elementos recursivamente versão 1")
listaOrdenada.printListaRecursivo(listaOrdenada._cabeca)
print(" ")

print("4.2) Imprimir elementos recursivamente versão 2")
listaOrdenada.plR()
print(" ")

print("5) Imprimir Lista Reversa")
listaOrdenada.printListaReversa()
print(" ")

print("6) Verificar se a lista está vazia")
print(listaOrdenada.esta_vazia())

print("7) Buscar recuperar um elemento da lista")
for i in range(13):
    if listaOrdenada.buscaElemento(i) != None:
        print(listaOrdenada.buscaElemento(i).valor())

print("8) Apagar alguns itens")
print("8.1 Listando os elementos antes")
listaOrdenada.printLista()

print("8.2 Removendo os elementos 15 (não existente), -5 (primeiro), 5 (último) e o -2 (intermediário)")
listaOrdenada.removeItem(15)  ## esse não existe
listaOrdenada.removeItem(-5)
listaOrdenada.removeItem(5)
listaOrdenada.removeItem(-2)

print("8.3 Listando os elementos depois")
listaOrdenada.printLista()

print("9) Remove com recursão (-4 e 2)")
listaOrdenada.removeItemRecursivamente(-4)
listaOrdenada.removeItemRecursivamente(2)
listaOrdenada.removeItemRecursivamente(-6)

print("Lista Finalmente")
listaOrdenada.printLista()

print("11) Verificando se duas listas são iguais")
lista1 = ListaEncadeadaOrdenada()
lista2 = ListaEncadeadaOrdenada()
print("11.1 Duas listas VAZIAS são iguais?")
print(lista1.saoIguais(lista2))
print("11.2 Uma lista VAZIA e outra com valores são iguais?")
lista1.inserirOrdenado(1)
print(lista1.saoIguais(lista2))
print("11.3 Uma lista com valores outra VAZIA são iguais?")
lista1 = ListaEncadeadaOrdenada()
lista2 = ListaEncadeadaOrdenada()
lista1.inserirOrdenado(3)
print(lista1.saoIguais(lista2))
print("11.4 Duas listas com diferentes quantidades de elementos são iguais?")
lista1 = ListaEncadeadaOrdenada()
lista2 = ListaEncadeadaOrdenada()
lista1.inserirOrdenado(4)
lista2.inserirOrdenado(1)
lista2.inserirOrdenado(3)
lista2.inserirOrdenado(4)
print(lista1.saoIguais(lista2))
print("11.5 Duas listas com diferentes elementos são iguais?")
lista1 = ListaEncadeadaOrdenada()
lista2 = ListaEncadeadaOrdenada()
lista1.inserirOrdenado(4)
lista2.inserirOrdenado(1)
print(lista1.saoIguais(lista2))
print("11.5 Duas listas idênticas são iguais?")
lista1 = ListaEncadeadaOrdenada()
lista2 = ListaEncadeadaOrdenada()
lista1.inserirOrdenado(3)
lista2.inserirOrdenado(3)
lista1.inserirOrdenado(-3)
lista2.inserirOrdenado(-3)
print(lista1.saoIguais(lista2))

print("10) Libera a memória")
listaOrdenada.libera()