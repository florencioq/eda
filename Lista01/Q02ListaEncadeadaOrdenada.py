import random
import sys
class ListaEncadeadaOrdenada:
    """ Lista encadeada ordenada de inteiros
    """

    class _No:
        """ Guardando um simples nó da lista
        """

        def __init__(self, inteiro, proximo):
            self._inteiro = inteiro
            self._proximo = proximo

        def valor(self):
            """ Retorna o campo Cadeia"""
            if self._inteiro != None:
                return str(self._inteiro)
            else:
                return "Sem Valor"

    def __init__(self):
        """
        :return: Cria uma lista encadeada em branco
        """
        self._cabeca = None

    def saoIguais(self, listaOrdenada):
        listasIguais=0
        lista1 = self._cabeca
        lista2 = listaOrdenada._cabeca
        if lista1 == lista2:
            return True
        else:
            while True:
                if lista1 == None and lista2 == None:
                    listasIguais = 1
                    break
                elif lista1 == None or lista2 == None:
                    break
                if lista1._inteiro == lista2._inteiro:
                    lista1 = lista1._proximo
                    lista2 = lista2._proximo
                else:
                    break
        return listasIguais==1

    def libera(self):
        self._cabeca = None

    def esta_vazia(self):
        """
        :return: retorna True se a lista está vazia e False se ela tem algum elemento
        """
        return self._cabeca == None

    def inserirOrdenado(self, numero):
        """
        :param elemento: elemento a ser inserido na lista encadeada
        :return:
        """
        ## Cria novo elemento
        novoElemento = self._No(numero, None)
        if self.esta_vazia():
            self._cabeca=novoElemento
        else:
            if numero <= self._cabeca._inteiro:
                novoElemento._proximo=self._cabeca
                self._cabeca=novoElemento
            else:
                elementoAnterior = self._cabeca
                elementoPosterior = self._cabeca
                while numero > elementoPosterior._inteiro:
                    if elementoPosterior != elementoAnterior:
                        elementoPosterior = elementoPosterior._proximo
                        elementoAnterior = elementoAnterior._proximo
                    else:
                        elementoPosterior = elementoPosterior._proximo
                    if elementoPosterior == None:
                        break
                elementoAnterior._proximo = novoElemento
                novoElemento._proximo = elementoPosterior

    def removeInicio(self):
        """
        :return: elemento removido ou Nome caso a lista esteja vazia
        """
        if self._cabeca != None:
            retornar = self._cabeca._inteiro
            self._cabeca = self._cabeca._proximo
            return retornar
        else:
            return None

    def removeItem(self, valor):
        """ Remove um item a partir de um inteiro """
        if not self.esta_vazia():
            ## Os dois ponteiros apontam pro primeiro elemento da lista
            elementoAnterior = self._cabeca
            elementoAtual = self._cabeca
            while True:
                ## Se o elemento for encontrado
                if elementoAtual._inteiro == valor:
                    while elementoAtual._inteiro == valor:
                        if elementoAtual==elementoAnterior:
                            ## Se o elemento a ser removido é o primeiro
                            self.removeInicio()
                            elementoAnterior = self._cabeca
                            elementoAtual = self._cabeca
                        else:
                            elementoAnterior._proximo=elementoAtual._proximo
                            elementoAtual = elementoAnterior._proximo
                            if elementoAtual == None:
                                break
                    break
                else:
                    ## se o elemento não foi encontrado ainda
                    if elementoAnterior!=elementoAtual:
                        ## Avança o ponteiro que marca o nó anterior apenas quando não é a primeira passagem
                        ## do Loop (os dois ponteiros já estão diferentes)
                        elementoAnterior=elementoAnterior._proximo
                    ## de qualquer forma avança o ponteiro para o atual
                    elementoAtual = elementoAtual._proximo
                    ## Testar se o elemento buscado não existe
                    if elementoAtual == None:
                        break
            return None

    def printLista(self):
        """
        :return: retorna sequencia com inteiros pertencentes à lista
        """
        lista=[]

        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                lista.append(elementoAtual._inteiro)
                if elementoAtual._proximo == None:
                    break
                else:
                    elementoAtual=elementoAtual._proximo
        print(lista)

    def removeItemRecursivamente(self, valor):
        """
        :param valor: inteiro a ser buscado para remoção do nó
        :return:
        """
        if not self.esta_vazia():
            if self._cabeca._inteiro != valor:
                novaLista = ListaEncadeadaOrdenada()
                novaLista._cabeca=self._cabeca._proximo
                self._cabeca._proximo = novaLista.removeItemRecursivamente(valor)
            else:
                while self._cabeca._inteiro == valor:
                    self.removeInicio()
        return self._cabeca

    def printListaRecursivo(self, noqualquer):
        """
        :return: imprime sequencia com inteiros pertencentes à lista de maneira recursiva
        """
        if noqualquer != None:
            sys.stdout.write(str(noqualquer._inteiro))
            sys.stdout.write(str(' '))
            self.printListaRecursivo(noqualquer._proximo)

    def plR(self):
        """
        :return: Imprime a lista recursivamente usando a Classe
        """
        if not self.esta_vazia():
            sys.stdout.write(str(self._cabeca._inteiro))
            sys.stdout.write(str(' '))
            novaLista = ListaEncadeadaOrdenada()
            novaLista._cabeca=self._cabeca._proximo
            novaLista.plR()

    def buscaElemento(self, numero):
        """ Buscar um nó através do número inteiro e retorna um Nó ou None se não encontrado"""
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                if elementoAtual._inteiro==numero:
                    return elementoAtual
                else:
                    elementoAtual = elementoAtual._proximo
                    if elementoAtual._proximo == None:
                        return None
        return None

    def printListaReversa(self):
        """
        :return: Imprime a lista de cauda para a cabeça
        """
        if not self.esta_vazia():
            novaLista = ListaEncadeadaOrdenada()
            novaLista._cabeca = self._cabeca._proximo
            novaLista.printListaReversa()
            sys.stdout.write(str(self._cabeca._inteiro))
            sys.stdout.write(str(' '))

if __name__=='__main__':

    print("1) Criar uma lista vazia")
    listaOrdenada = ListaEncadeadaOrdenada()

    print("6) Verificar se a lista esta vazia")
    print(listaOrdenada.esta_vazia())

    print("2) Inserir elementos no início da lista")
    for n in range(40):
        listaOrdenada.inserirOrdenado(random.randint(-5,5))
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