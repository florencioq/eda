from Lista01.Q01ListaEncadeadaInteira import *

print("1) Criar uma lista vazia")
listaSimples = ListaEncadeada()

print("6) Verificar se a lista esta vazia")
print(listaSimples.esta_vazia())

print("2) Inserir elementos no início da lista")
for n in range(-10, 14, 2):
    listaSimples.inserirInicio(n)

print("3) Imprimir elementos de uma lista encadeada")
listaSimples.printLista()

print("4.1) Imprimir elementos recursivamente versão 1")
listaSimples.printListaRecursivo(listaSimples._cabeca)

print("4.2) Imprimir elementos recursivamente versão 2")
listaSimples.plR()

print("5) Imprimir Lista Reversa")
listaSimples.printListaReversa()

print("6) Verificar se a lista está vazia")
print(listaSimples.esta_vazia())

print("7) Buscar recuperar um elemento da lista")
for i in range(13):
    if listaSimples.buscaElemento(i) != None:
        print(listaSimples.buscaElemento(i).valor())

print("8) Apagar alguns itens")
print("8.1 Listando os elementos antes")
listaSimples.printLista()

print("8.2 Removendo os elementos 15, 6, 4 e o -2")
listaSimples.removeItem(15)  ## esse não existe
listaSimples.removeItem(6)
listaSimples.removeItem(4)
listaSimples.removeItem(-2)

print("8.3 Listando os elementos depois")
listaSimples.printLista()

print("9) Remove itens recursivamente (12, 0, -10)")
listaSimples.removeItemRecursivamente(12)
listaSimples.removeItemRecursivamente(0)
listaSimples.removeItemRecursivamente(-10)
print("9.1 Listando os elementos depois")
listaSimples.printLista()

print("10) Libera lista")
listaSimples.libera()