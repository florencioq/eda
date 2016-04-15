from random import *

class HashTable:
    def __init__(self, tamanho=20):
        self._tabela = tamanho * [None]
        self._n = 0
        self._primo = 109345121
        self._a = 1+randrange(self._primo-1)
        self._b = randrange(self._primo)

        self.colisoes = 0

    def tamanho(self):
        return self._n

    def _funcao_hash(self, k):
        tam = len(self._tabela)
        return (k * self._a + self._b) % self._primo % tam

    def setitem(self, k):
        j = self._funcao_hash(k)
        if self._tabela[j]==1:
            self.colisoes+=1
        else:
            self._tabela[j]=1

if __name__=='__main__':

    n = int(input("Entre com o tamanho do vetor: "))
    myHashTable = HashTable(n)

    print(myHashTable.tamanho())
    print(myHashTable.colisoes)
    for i in range(200,1600,5):
        myHashTable.setitem(i)
    print(myHashTable.colisoes)

