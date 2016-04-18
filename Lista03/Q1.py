from random import *

class HashTable:
    def __init__(self, tamanho=20):
        self._tabela = tamanho * [None]
        self._n = 0
        self._primo = 109345121
        self._a = 1 + randrange(self._primo - 1)
        self._a = 787687
        self._b = randrange(self._primo)
        self._b = 554755
        self.colisoes = 0

    def libera(self):
        self._tabela = None

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
                print("None")
            else:
                print(str(self._tabela[i]._chave) + " "+ str( self._tabela[i]._valor))

    def remitem(self, k):
        jj = self._funcao_hash(k)
        j = jj
        naoAchou = False
        while self._tabela[j] == None or self._tabela[j]._chave != k:
            j += 1
            if j == len(self._tabela):
                ## Chegou ao final
                j = 0
                while self._tabela[j] == None or self._tabela[j]._chave != k:
                    j += 1
                    if j == jj or j == len(self._tabela):
                        naoAchou = True
                        break
            if naoAchou:
                break
        if naoAchou:
            return False
        else:
            self._tabela[j] = None
            return True

    def getitem(self, k):
        jj = self._funcao_hash(k)
        j = jj
        naoAchou = False
        while self._tabela[j] == None or self._tabela[j]._chave != k:
            j += 1
            if j == len(self._tabela):
                ## Chegou ao final
                j = 0
                while self._tabela[j] == None or self._tabela[j]._chave != k:
                    j += 1
                    if j == jj or j == len(self._tabela):
                        naoAchou = True
                        break
            if naoAchou:
                break
        if naoAchou:
            return None
        else:
            return self._tabela[j]._valor


    def setitem(self, k, num):
        jj = self._funcao_hash(k)
        j = jj
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
                # Circulando
                j = 0
                while j < jj and self._tabela[j] != None:
                    j += 1
                if j == jj:
                    hashCheio = True
                else:
                    self._tabela[j] = elemento
                    self._n += 1
                    hashCheio = False
            else:
                self._tabela[j] = elemento
                self._n += 1
                hashCheio = False
        if hashCheio:
            return False
        else:
            return True


if __name__ == '__main__':

    n = int(input("Entre com o número de chaves: "))

    # O bucket terá a metade do numero de chaves
    myHashTable = HashTable(int(n/2))

    print("Incluindo alguns elementos")
    print("=========================")
    for i in range(1,n+1):
        if not myHashTable.setitem(i, randint(1, 1000)):
            print("Colisão")
        print("-------------------------")
        myHashTable._printHash()
    print("=========================")
    print("Buscando alguns elementos")
    print("=========================")
    for i in range(1,n+1):
        retorno = myHashTable.getitem(i)
        if retorno != None:
            print(str(i)+"-"+str(retorno))
    print("=========================")
    print("Eliminando alguns elementos")
    print("=========================")
    for i in range (1,n,2):
        retorno = myHashTable.remitem(i)
    myHashTable._printHash()

    print("=========================")
    print("Liberando a memória")
    print("=========================")
    myHashTable.libera()

    del myHashTable
