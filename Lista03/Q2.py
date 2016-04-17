from random import *

class HashTable:
    class _Bucket:
        def __init__(self, tamanho=20):
            self._tabela = tamanho * [None]

    def __init__(self, tamanho=20):
        ## Atributos da função de hash
        self._primo = 109345121
        self._a = 1 + randrange(self._primo - 1)
        self._a = 787687
        self._b = randrange(self._primo)
        self._b = 554755

        # Tamanho total do Hash
        self.tamanho = tamanho

        ## Indice
        self.dicionario = {0: self._Bucket(), 1: self._Bucket()}

        ## Número de bits de indexação
        self.profundidade = 1


    class _Elemento:
        def __init__(self, chave, num):
            self._chave = chave
            self._valor = num

    def _funcao_hash(self, k):
        tam = len(self.dicionario[0]._tabela)
        return (k * self._a + self._b) % self._primo % tam

    def print(self):
        print("Docionario")
        print(self.dicionario)
        print("Buckets")
        for k, v in self.dicionario.items():
            print("Bucket " + str(k))
            for i in v._tabela:
                if i != None:
                    print(str(k) + "-" + str(i._valor))

    def setitem(self, k, num):
        kj = self._funcao_hash(k)  # hash
        d = self.profundidade  # profundidade em bits
        r = kj & pow(2, d) - 1  # reduzindo a chave ao numero bits da profundidade
        bucket = self.dicionario[r]  # encontrar o ponteiro pro bucket
        kkj = kj >> d  # retiro os bits de indexação para usar o restante para fazer hash no bucket

        # de posse de bucket vamos preenche-lo
        elemento = self._Elemento(k, num)
        kkjj = kkj
        if bucket._tabela[kkjj] == None:
            bucket._tabela[kkjj] = elemento

if __name__ == '__main__':

    n = int(input("Entre com o número de chaves: "))

    # A Hash terá a metade do numero de chaves
    myHashTable = HashTable(int(n))

    print("Incluindo alguns elementos")
    print("=========================")
    for i in range(1,n+1):
        myHashTable.setitem(i, randint(1, 1000))
    myHashTable.print()
