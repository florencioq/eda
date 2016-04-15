from random import *


class HashTable:
    def __init__(self, tamanho=20):
        self._tabela = tamanho * [None]
        self._n = 0
        self._primo = 109345121
        self._a = 1 + randrange(self._primo - 1)
        self._b = randrange(self._primo)
        self.colisoes = 0

    class _Elemento:
        def __init__(self, chave, num):
            self._chave = chave
            self._valor = num

    def tamanho(self):
        return len(self._tabela)

    def _funcao_hash(self, k):
        tam = len(self._tabela)
        return (k * self._a + self._b) % self._primo % tam

    def _printHash(self):
        for i in range(len(self._tabela)):
            if self._tabela[i] == None:
                print(0)
            else:
                print(str(self._tabela[i]._chave) + " "+ str( self._tabela[i]._valor))

    def getitem(self, k):
        j = self._funcao_hash(k)
        if self._tabela[j]._chave == k:
            return self._tabela[j]._valor
        else:
            while self._tabela[j]._chave != k and j < self.tamanho():
                j += 1
            if self._tabela[j]._chave == k:
                return self._tabela[j]._valor
            else:
                return None

    def setitem(self, k, num):
        j = self._funcao_hash(k)
        elemento = self._Elemento(k, num)

        ## Buscando o elemento
        if self._tabela[j] == None:
            self._tabela[j] = elemento
            self._n += 1
            hashCheio = False
        else:
            self.colisoes += 1
            while j < self.tamanho() and self._tabela[j] != None:
                j += 1
            if j == self.tamanho():
                hashCheio = True
            else:
                self._tabela[j] = elemento
                self._n += 1
                hashCheio = False
        if hashCheio:
            return False
        else:
            return True


if __name__ == '__main__':

    n = int(input("Entre com o tamanho do vetor: "))
    myHashTable = HashTable(int(n/2))

    print(myHashTable.tamanho())
    print(myHashTable.colisoes)
    print("=================")
    for i in range(1,n+1):
        if not myHashTable.setitem(i, randint(1, 1000)):
            print("Colisão")
        print("------------")
        myHashTable._printHash()
    print("=================")
    print(myHashTable.colisoes)
