import random
import sys

class ListaDuplamenteEncadeadaOrdenadaCircular:
    """ Lista encadeada ordenada de inteiros
    """

    class _No:
        """ Guardando um simples nó da lista
        """

        def __init__(self, inteiro, anterior, proximo):
            self._inteiro = inteiro
            self._proximo = proximo
            self._anterior = anterior

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
        listasIguais = 0
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
        return listasIguais == 1

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
        novoElemento = self._No(numero, None, None)
        if self.esta_vazia():
            self._cabeca = novoElemento
            self._cabeca._proximo = novoElemento
            self._cabeca._anterior = novoElemento
        else:
            if numero <= self._cabeca._inteiro:
                novoElemento._proximo = self._cabeca
                novoElemento._anterior = self._cabeca._anterior
                self._cabeca._anterior._proximo = novoElemento
                self._cabeca._anterior = novoElemento
                self._cabeca = novoElemento
                # Girar procurando acertar o giro da lista circular
                # elementoGiro = novoElemento._proximo
                # while elementoGiro._proximo != novoElemento._proximo:
                #     elementoGiro = elementoGiro._proximo
                # elementoGiro._proximo = novoElemento
                # self._cabeca._anterior = novoElemento
            else:
                elementoAnterior = self._cabeca
                elementoPosterior = self._cabeca
                while numero > elementoPosterior._inteiro:
                    if elementoPosterior != elementoAnterior:
                        elementoPosterior = elementoPosterior._proximo
                        elementoAnterior = elementoAnterior._proximo
                    else:
                        elementoPosterior = elementoPosterior._proximo
                    if elementoPosterior == self._cabeca:
                        break
                elementoAnterior._proximo = novoElemento
                novoElemento._proximo = elementoPosterior
                elementoPosterior._anterior = novoElemento
                novoElemento._anterior = elementoAnterior

    def removeInicio(self):
        """
        :return: elemento removido ou None caso a lista esteja vazia
        """
        if self._cabeca != None:
            retornar = self._cabeca._inteiro

            # só tem 1 elemento
            if self._cabeca == self._cabeca._proximo:
                self._cabeca = None
                return retornar

            self._cabeca._proximo._anterior = self._cabeca._anterior
            self._cabeca._anterior._proximo = self._cabeca._proximo
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
                        if elementoAtual == elementoAnterior:
                            ## Se o elemento a ser removido é o primeiro
                            self.removeInicio()
                            elementoAnterior = self._cabeca
                            elementoAtual = self._cabeca
                        else:
                            elementoAnterior._proximo = elementoAtual._proximo
                            elementoAnterior._proximo._anterior = elementoAnterior
                            elementoAtual = elementoAnterior._proximo
                            if elementoAtual == self._cabeca:
                                break
                    break
                else:
                    ## se o elemento não foi encontrado ainda
                    if elementoAnterior != elementoAtual:
                        ## Avança o ponteiro que marca o nó anterior apenas quando não é a primeira passagem
                        ## do Loop (os dois ponteiros já estão diferentes)
                        elementoAnterior = elementoAnterior._proximo
                    ## de qualquer forma avança o ponteiro para o atual
                    elementoAtual = elementoAtual._proximo
                    ## Testar se o elemento buscado não existe
                    if elementoAtual == self._cabeca:
                        break
            return None

    def removeItemRecursivamente(self, valor):
        """
        :param valor: inteiro a ser buscado para remoção do nó
        :return:
        """
        if not self.esta_vazia():
            if self._cabeca._inteiro != valor:

                # Se tem apenas 1 elemento, acabou
                if self._cabeca == self._cabeca._proximo:
                    return self._cabeca

                novaLista = ListaDuplamenteEncadeadaOrdenadaCircular()
                novaLista._cabeca = self._cabeca._proximo
                novaLista._cabeca._anterior = self._cabeca._anterior
                novaLista._cabeca._anterior._proximo = novaLista._cabeca

                # Recursão
                novoProximo = novaLista.removeItemRecursivamente(valor)

                if novoProximo == None: # Fim da lista
                    self._cabeca._proximo = self._cabeca
                    self._cabeca._anterior = self._cabeca
                else:
                    # Abrir o laço da lista
                    self._cabeca._anterior = novoProximo._anterior
                    self._cabeca._proximo = novoProximo
                    novoProximo._anterior._proximo = self._cabeca
                    novoProximo._anterior = self._cabeca
            else:
                while self._cabeca._inteiro == valor:
                    self.removeInicio()
                    if self._cabeca == None:
                        break
        return self._cabeca

    def printListaRecursivo(self):
        """
        :return: Imprime a lista recursivamente usando a Classe
        """
        if not self.esta_vazia():
            sys.stdout.write(str(self._cabeca._inteiro))
            sys.stdout.write(str(' '))

            # Se tem apenas 1 elemento, acabou
            if self._cabeca == self._cabeca._proximo:
                return

            novaLista = ListaDuplamenteEncadeadaOrdenadaCircular()
            novaLista._cabeca = self._cabeca._proximo
            elementoGiro = novaLista._cabeca
            while elementoGiro._proximo != self._cabeca:
                elementoGiro = elementoGiro._proximo
            elementoGiro._proximo = self._cabeca._proximo

            novaLista.printListaRecursivo()

            elementoGiro = novaLista._cabeca
            while elementoGiro._proximo != self._cabeca._proximo:
                elementoGiro = elementoGiro._proximo
            elementoGiro._proximo = self._cabeca

    def buscaElemento(self, numero):
        """ Buscar um nó através do número inteiro e retorna um Nó ou None se não encontrado"""
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                if elementoAtual._inteiro == numero:
                    return numero
                else:
                    if elementoAtual._proximo == self._cabeca:
                        return None
                    else:
                        elementoAtual = elementoAtual._proximo

        return None

    def printLista(self):
        """
        :return: retorna sequencia com inteiros pertencentes à lista
        """

        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                sys.stdout.write(str(elementoAtual._inteiro))
                sys.stdout.write(str(' '))
                if elementoAtual._proximo == self._cabeca:
                    break
                else:
                    elementoAtual = elementoAtual._proximo
            print(" ")

    def printListaReverso(self):
        """
        :return: retorna sequencia com inteiros pertencentes à lista
        """
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                sys.stdout.write(str(elementoAtual._inteiro))
                sys.stdout.write(str(' '))
                if elementoAtual._anterior == self._cabeca:
                    break
                else:
                    elementoAtual = elementoAtual._anterior
            print(" ")

if __name__ == '__main__':

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
