class ListaEncadeada:
    """ Lista encadeada simples de inteiros
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

    def libera(self):
        self._cabeca = None;

    def esta_vazia(self):
        """
        :return: retorna True se a lista está vazia e False se ela tem algum elemento
        """
        return self._cabeca == None

    def inserirInicio(self, numero):
        """
        :param elemento: elemento a ser inserido na lista encadeada
        :return:
        """
        self._cabeca = self._No(numero, self._cabeca)

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

    def removeItemRecursivamente(self, valor):
        """
        :param valor: inteiro a ser buscado para remoção do nó
        :return:
        """
        if not self.esta_vazia():
            if self._cabeca._inteiro != valor:
                novaLista = ListaEncadeada()
                novaLista._cabeca=self._cabeca._proximo
                self._cabeca._proximo = novaLista.removeItemRecursivamente(valor)
            else:
                self.removeInicio()
        return self._cabeca

    def removeItem(self, valor):
        """ Remove um item a partir de um inteiro """
        if not self.esta_vazia():
            ## Os dois ponteiros apontam pro primeiro elemento da lista
            elementoAnterior = self._cabeca
            elementoAtual = self._cabeca
            while True:
                ## Se o elemento for encontrado
                if elementoAtual._inteiro == valor:
                    if elementoAtual==elementoAnterior:
                        ## Se o elemento a ser removido é o primeiro
                        self.removeInicio()
                    else:
                        elementoAnterior._proximo=elementoAtual._proximo
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

    def printListaRecursivo(self, noqualquer):
        """
        :return: imprime sequencia com inteiros pertencentes à lista de maneira recursiva
        """
        if noqualquer != None:
            print(noqualquer._inteiro)
            self.printListaRecursivo(noqualquer._proximo)

    def plR(self):
        """
        :return: Imprime a lista recursivamente usando a Classe
        """
        if not self.esta_vazia():
            print(self._cabeca._inteiro)
            novaLista = ListaEncadeada()
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
            novaLista = ListaEncadeada()
            novaLista._cabeca = self._cabeca._proximo
            novaLista.printListaReversa()
            print(self._cabeca._inteiro)

if __name__=='__main__':

    print("1) Criar uma lista vazia")
    listaSimples = ListaEncadeada()

    print("6) Verificar se a lista esta vazia")
    print(listaSimples.esta_vazia())

    print("2) Inserir elementos no início da lista")
    for n in range(-10,14,2):
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