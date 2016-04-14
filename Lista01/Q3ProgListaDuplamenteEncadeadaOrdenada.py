from Lista01.Q03ListaDuplamenteEncadeadaOrdenada import *

print("1) Criar uma lista vazia")
listaDuplamenteEncadeadaOrdenada = ListaDuplamenteEncadeadaOrdenada()

print("6) Verificar se a lista esta vazia")
print(listaDuplamenteEncadeadaOrdenada.esta_vazia())

print("2) Inserir elementos no início da lista")
for n in range(40):
    listaDuplamenteEncadeadaOrdenada.inserirOrdenado(random.randint(-5, 5))
    listaDuplamenteEncadeadaOrdenada.printLista()
    listaDuplamenteEncadeadaOrdenada.printListaReverso()

print("3) Imprimir elementos de uma lista encadeada")
listaDuplamenteEncadeadaOrdenada.printLista()

print("4.1) Imprimir elementos recursivamente versão 1")
listaDuplamenteEncadeadaOrdenada.printListaRecursivo(listaDuplamenteEncadeadaOrdenada._cabeca)
print(" ")

print("4.2) Imprimir elementos recursivamente versão 2")
listaDuplamenteEncadeadaOrdenada.plR()
print(" ")

print("5) Imprimir Lista Reversa")
listaDuplamenteEncadeadaOrdenada.printListaReverso()

print("6) Verificar se a lista está vazia")
print(listaDuplamenteEncadeadaOrdenada.esta_vazia())

print("7) Buscar recuperar um elemento da lista")
for i in range(13):
    if listaDuplamenteEncadeadaOrdenada.buscaElemento(i) != None:
        print(listaDuplamenteEncadeadaOrdenada.buscaElemento(i).valor())

print("8) Apagar alguns itens")
print("8.1 Listando os elementos antes")
listaDuplamenteEncadeadaOrdenada.printLista()
listaDuplamenteEncadeadaOrdenada.printListaReverso()

print("8.2 Removendo os elementos 15 (não existente), -5 (primeiro), 5 (último) e o -2 (intermediário)")
listaDuplamenteEncadeadaOrdenada.removeItem(15)  ## esse não existe
listaDuplamenteEncadeadaOrdenada.removeItem(-5)
listaDuplamenteEncadeadaOrdenada.removeItem(5)
listaDuplamenteEncadeadaOrdenada.removeItem(-2)

print("8.3 Listando os elementos depois")
listaDuplamenteEncadeadaOrdenada.printLista()
listaDuplamenteEncadeadaOrdenada.printListaReverso()

print("9) Remove com recursão (-4, 2, 4 e 6)")
listaDuplamenteEncadeadaOrdenada.removeItemRecursivamente(-4)
listaDuplamenteEncadeadaOrdenada.printLista()
listaDuplamenteEncadeadaOrdenada.printListaReverso()
listaDuplamenteEncadeadaOrdenada.removeItemRecursivamente(2)
listaDuplamenteEncadeadaOrdenada.printLista()
listaDuplamenteEncadeadaOrdenada.printListaReverso()
listaDuplamenteEncadeadaOrdenada.removeItemRecursivamente(4)
listaDuplamenteEncadeadaOrdenada.printLista()
listaDuplamenteEncadeadaOrdenada.printListaReverso()

print("Lista Finalmente")
listaDuplamenteEncadeadaOrdenada.printLista()
listaDuplamenteEncadeadaOrdenada.printListaReverso()

print("11) Verificando se duas listas são iguais")
lista1 = ListaDuplamenteEncadeadaOrdenada()
lista2 = ListaDuplamenteEncadeadaOrdenada()
print("11.1 Duas listas VAZIAS são iguais?")
print(lista1.saoIguais(lista2))
print("11.2 Uma lista VAZIA e outra com valores são iguais?")
lista1.inserirOrdenado(1)
print(lista1.saoIguais(lista2))
print("11.3 Uma lista com valores outra VAZIA são iguais?")
lista1 = ListaDuplamenteEncadeadaOrdenada()
lista2 = ListaDuplamenteEncadeadaOrdenada()
lista1.inserirOrdenado(3)
print(lista1.saoIguais(lista2))
print("11.4 Duas listas com diferentes quantidades de elementos são iguais?")
lista1 = ListaDuplamenteEncadeadaOrdenada()
lista2 = ListaDuplamenteEncadeadaOrdenada()
lista1.inserirOrdenado(4)
lista2.inserirOrdenado(1)
lista2.inserirOrdenado(3)
lista2.inserirOrdenado(4)
print(lista1.saoIguais(lista2))
print("11.5 Duas listas com diferentes elementos são iguais?")
lista1 = ListaDuplamenteEncadeadaOrdenada()
lista2 = ListaDuplamenteEncadeadaOrdenada()
lista1.inserirOrdenado(4)
lista2.inserirOrdenado(1)
print(lista1.saoIguais(lista2))
print("11.5 Duas listas idênticas são iguais?")
lista1 = ListaDuplamenteEncadeadaOrdenada()
lista2 = ListaDuplamenteEncadeadaOrdenada()
lista1.inserirOrdenado(3)
lista2.inserirOrdenado(3)
lista1.inserirOrdenado(-3)
lista2.inserirOrdenado(-3)
print(lista1.saoIguais(lista2))

print("10) Libera a memória")
listaDuplamenteEncadeadaOrdenada.libera()