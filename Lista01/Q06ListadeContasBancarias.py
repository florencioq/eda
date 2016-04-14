import sys

class ContaBancaria:
    """ Uma conta bancária comum """

    def __init__(self, numero, saldo, limite):
        """ Cria uma instância da Conta Bancária"""
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    def efetuar_debito(self, valor):
        """ Efetua débitos na Conta Bancária"""
        if valor <= self._limite + self._saldo:
            self._saldo = self._saldo - valor
            return True
        else:
            return False

    def efetuar_credito(self, valor):
        """ Efetua créditos na Conta Bancária"""
        self._saldo = self._saldo + valor

    def get_saldo(self):
        return self._saldo

    def get_numero(self):
        return  self._numero

    def get_detalhes(self):
        return "Conta: "+str(self._numero)+" Saldo: "+str(self._saldo) + " Limite: " + str(self._limite)

class ContaPoupanca(ContaBancaria):
    """ Uma conta poupança"""

    def render_juros(self, taxa):
        self.efetuar_credito(self._saldo * taxa)


class ContaFidelidade(ContaBancaria):
    """ Uma conta bônus"""

    def __init__(self, numero, saldo, limite, bonus):
        super().__init__(numero, saldo, limite)
        self._bonus = bonus

    def efetuar_credito(self, valor):
        self._bonus = self._bonus + 0.01 * valor
        super().efetuar_credito(valor)

    def render_bonus(self):
        super().efetuar_credito(self._bonus)
        self._bonus = 0

    def get_bonus(self):
        return self._bonus

    def get_detalhes(self):
        return "Conta: "+str(self._numero)+" Saldo: "+str(self._saldo) + " Limite: " + str(self._limite)+ " Bônus: "+str(self._bonus)

class ListadeContasBancarias:

    class _No:
        """ Guardando um simples nó da lista
        """
        def __init__(self, conta, proximo):
            self._conta = conta
            self._proximo = proximo

    def __init__(self):
        self._cabeca = None

    def render_bonus(self, conta):
        conta = self.buscaElemento(conta)
        if conta != None:
            try:
                conta._conta.render_bonus()
                return True
            except:
                None
        return False

    def render_juros(self, conta, taxa):
        conta = self.buscaElemento(conta)
        if conta != None:
            try:
                conta._conta.render_juros(taxa)
                return True
            except:
                None
        return False

    def efetuar_credito(self, conta, valor):
        conta = self.buscaElemento(conta)
        if conta != None:
            conta._conta.efetuar_credito(valor)
            return True
        else:
            return False

    def efetuar_debito(self, conta, valor):
        conta = self.buscaElemento(conta)
        if conta != None:
            if conta._conta.efetuar_debito(valor):
                return True
            else:
                return False
        else:
            return False

    def efetuar_transferencia(self, contaDebito, contaCredito, valor):
        contaCredito = self.buscaElemento(contaCredito)
        contaDebito = self.buscaElemento(contaDebito)
        # Primeiro temos que realizar o debito com sucesso, apenas depois o crédito
        if contaDebito._conta.efetuar_debito(valor):
            contaCredito._conta.efetuar_credito(valor)
            return True
        else:
            return False

    def get_saldo(self, conta):
        conta = self.buscaElemento(conta)
        if conta != None:
            return conta._conta.get_saldo()
        else:
            return False

    def get_bonus(self, conta):
        conta = self.buscaElemento(conta)
        if conta != None:
            try:
                bonus = conta._conta.get_bonus()
            except:
                bonus = None
            return bonus
        else:
            return False

    def esta_vazia(self):
        """
        :return: retorna True se a lista está vazia e False se ela tem algum elemento
        """
        return self._cabeca == None

    def libera(self):
        self._cabeca = None

    def removeInicio(self):
        """
        :return: elemento removido ou Nome caso a lista esteja vazia
        """
        if not self.esta_vazia():
            self._cabeca = self._cabeca._proximo

    def removeItemRecursivamente(self, valor):
        """
        :param valor: inteiro a ser buscado para remoção do nó
        :return:
        """
        if not self.esta_vazia():
            if self._cabeca._conta._numero != valor:
                novaLista = ListadeContasBancarias()
                novaLista._cabeca=self._cabeca._proximo
                self._cabeca._proximo = novaLista.removeItemRecursivamente(valor)
            else:
                while self._cabeca._conta._numero == valor:
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
                if elementoAtual._conta._numero == valor:
                    while elementoAtual._conta._numero == valor:
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

    def buscaElemento(self, numero):
        """ Buscar um nó através do número inteiro e retorna um Nó ou None se não encontrado"""
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                if elementoAtual._conta._numero==numero:
                    return elementoAtual
                else:
                    elementoAtual = elementoAtual._proximo
                    if elementoAtual == None:
                        return None
        return None

    def printListaRecursivo(self):
        """
        :return: Imprime a lista recursivamente usando a Classe
        """
        if not self.esta_vazia():
            sys.stdout.write(str(self._cabeca._conta._numero))
            sys.stdout.write(str(' '))
            novaLista = ListadeContasBancarias()
            novaLista._cabeca=self._cabeca._proximo
            novaLista.printListaRecursivo()

    def printLista(self):
        """
        :return: retorna sequencia com inteiros pertencentes à lista
        """
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                sys.stdout.write(str(elementoAtual._conta._numero))
                sys.stdout.write(str(' '))
                if elementoAtual._proximo == None:
                    break
                else:
                    elementoAtual = elementoAtual._proximo
            print("")

    def printContasLista(self):
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                sys.stdout.write("Conta: "+str(elementoAtual._conta._numero)+" Saldo: "+str(elementoAtual._conta.get_saldo()))
                print("")
                if elementoAtual._proximo == None:
                    break
                else:
                    elementoAtual = elementoAtual._proximo

    def printDetalhesLista(self):
        if not self.esta_vazia():
            elementoAtual = self._cabeca
            while True:
                sys.stdout.write(elementoAtual._conta.get_detalhes())
                print("")
                if elementoAtual._proximo == None:
                    break
                else:
                    elementoAtual = elementoAtual._proximo

    def printListaReversa(self):
        """
        :return: Imprime a lista de cauda para a cabeça
        """
        if not self.esta_vazia():
            novaLista = ListadeContasBancarias()
            novaLista._cabeca = self._cabeca._proximo
            novaLista.printListaReversa()
            sys.stdout.write(str(self._cabeca._conta._numero))
            sys.stdout.write(str(' '))

    def inserirOrdenado(self, numero):
        """
        :param elemento: elemento a ser inserido na lista encadeada
        :return:
        """
        ## Cria novo elemento
        novoElemento = self._No(numero, None)
        if self.esta_vazia():
            self._cabeca = novoElemento
        else:
            if numero._numero <= self._cabeca._conta._numero:
                novoElemento._proximo = self._cabeca
                self._cabeca = novoElemento
            else:
                elementoAnterior = self._cabeca
                elementoPosterior = self._cabeca
                while numero._numero > elementoPosterior._conta._numero:
                    if elementoPosterior != elementoAnterior:
                        elementoPosterior = elementoPosterior._proximo
                        elementoAnterior = elementoAnterior._proximo
                    else:
                        elementoPosterior = elementoPosterior._proximo
                    if elementoPosterior == None:
                        break
                elementoAnterior._proximo = novoElemento
                novoElemento._proximo = elementoPosterior

if __name__ == '__main__':
    print("Criando a lista de contas")
    listadeContas = ListadeContasBancarias()
    print("")
    print("Lista está vazia?")
    print(listadeContas.esta_vazia())
    print("")
    print("Criando Conta Corrente")
    contaBancaria5234 = ContaBancaria(5234,100,100)

    print("Criando Conta Poupança")
    contaPoupanca2346 = ContaPoupanca(2346,150,0)

    print("Criando Conta Fidelidade")
    contaFidelidade3247 = ContaFidelidade(3247,200,200,0)

    print("Criando Conta Fidelidade")
    contaFidelidade3657 = ContaFidelidade(3657,200,250,0)
    print("")
    print("Inserindo na lista")
    listadeContas.inserirOrdenado(contaBancaria5234)
    listadeContas.inserirOrdenado(contaPoupanca2346)
    listadeContas.inserirOrdenado(contaFidelidade3247)
    listadeContas.inserirOrdenado(contaFidelidade3657)
    print("")
    print("Impressão direta")
    listadeContas.printLista()
    print("")
    print("Impressão recursiva")
    listadeContas.printListaRecursivo()
    print("")
    print("")
    print("Impressão Reversa")
    listadeContas.printListaReversa()
    print("")
    print("")
    print("Lista está vazia?")
    print(listadeContas.esta_vazia())
    print("")

    print("Buscando uma conta existente")
    print(listadeContas.buscaElemento(5234)._conta._numero)
    print("")

    print("Buscando uma conta inexistente")
    contaBuscada = listadeContas.buscaElemento(3421)
    if contaBuscada != None:
        print(contaBuscada._conta._numero)
    else:
        print("Conta não encontrada")
    print("")

    print("Removendo um determinado elemento (5234) da lista")
    listadeContas.removeItem(5234)
    listadeContas.printLista()
    print("")

    print("Criando Conta Corrente 6765")
    contaBancaria6765 = ContaBancaria(6765,100,80)
    listadeContas.inserirOrdenado(contaBancaria6765)
    listadeContas.printLista()
    print("")

    print("Removendo itens (3247) recursivamente")
    listadeContas.removeItemRecursivamente(3247)
    listadeContas.printLista()
    print("")

    print("Listando as contas e saldos")
    listadeContas.printContasLista()
    print("")
    print("Efetuando crédito de 80,00 na conta 6765")
    listadeContas.efetuar_credito(6765,80)
    print("Saldo da Conta 6765: ")
    print(listadeContas.get_saldo(6765))
    print("")
    print("Listando as contas e saldos")
    listadeContas.printContasLista()
    print("")
    print("Listando mais flexível com detalhes:")
    listadeContas.printDetalhesLista()
    print("")
    print("Fazendo uns creditos em conta fidelidade 3657:")
    print("120 na conta 3657")
    print("Novos saldos:")
    listadeContas.efetuar_credito(3657,120)
    listadeContas.printDetalhesLista()
    print("Consultando o bônus da conta 3657:")
    print(listadeContas.get_bonus(3657))
    print("Consultando o bônus de conta não fidelidade:")
    print(listadeContas.get_bonus(6765))
    print("Listando os detalhes:")
    listadeContas.printDetalhesLista()
    print("Fazendo um débito maior que o saldo+limite:")
    print("Debitando 200 na conta 2346:")
    if listadeContas.efetuar_debito(2346,200):
        print("Sucesso!")
        listadeContas.printDetalhesLista()
    else:
        print("Falha!")
    print("")
    print("Fazendo uma transferência que dá certo")
    listadeContas.printDetalhesLista()
    print("Operação: 100 da conta 3657 para a conta 2346")
    if listadeContas.efetuar_transferencia(3657,2346,100):
        print("Sucesso!")
    else:
        print("Falha")
    listadeContas.printDetalhesLista()

    print("")
    print("Fazendo uma transferência que falha")
    listadeContas.printDetalhesLista()
    print("Operação: 400 da conta 6765 para a conta 3657")
    if listadeContas.efetuar_transferencia(6765, 3657, 400):
        print("Sucesso!")
    else:
        print("Falha")
    listadeContas.printDetalhesLista()

    print("")
    print("Render juros em poupança 5% conta 2346")
    listadeContas.render_juros(2346,0.05)
    listadeContas.printDetalhesLista()

    print("")
    print("Render bônus conta 3657")
    listadeContas.render_bonus(3657)
    listadeContas.printDetalhesLista()

    print("Liberando a Lista")
    listadeContas.libera()
