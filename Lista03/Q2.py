from random import *

class HashTable:
    class _Bucket:
        def __init__(self, tamanho=20):
            self._tabela = tamanho * [None]

    def __init__(self, tambucket=10):
        ## Atributos da função de hash
        self._primo = 109345121
        self._a = 1 + randrange(self._primo - 1)
        self._a = 787687
        self._b = randrange(self._primo)
        self._b = 554755

        self._tambucket = tambucket

        ## Indice
        self.dicionario = {0: self._Bucket(tambucket), 1: self._Bucket(tambucket)}

    def profundidade(self):
        tamdict = len(self.dicionario)
        numbitdict = (tamdict - 1).bit_length()
        return numbitdict

    ## Adiciona um bit a mais no dicionario e mantem ponteiros
    def ampliadict(self):
        tamdict = len(self.dicionario)
        numbitdict = (tamdict - 1).bit_length()
        novoDict = {}
        for i in range(pow(2, numbitdict + 1)):
            if i < tamdict:
                novoDict[i] = self.dicionario[i]
            else:
                novoDict[i] = self.dicionario[i & pow(2, numbitdict) - 1]
        return novoDict

    def tamanho(self):
        tamdict = len(self.dicionario)
        tambucket = len(self.dicionario[0]._tabela)
        return tamdict * tambucket

    class _Elemento:
        def __init__(self, chave, num):
            self._chave = chave
            self._valor = num

    def _funcao_hash(self, k):
        tam = self.tamanho()
        return (k * self._a + self._b) % self._primo % tam

    def print(self):
        print("Docionario")
        print(self.dicionario)
        print("Buckets")
        for k, v in self.dicionario.items():
            print("Bucket " + str(k))
            for i in v._tabela:
                if i != None:
                    print(str(k) + "-" + str(i._chave) + "-" + str(i._valor))

    def delitem(self, k):
        kj = self._funcao_hash(k)  # hash
        d = self.profundidade()  # profundidade em bits
        r = kj & pow(2, d) - 1  # reduzindo a chave ao numero bits da profundidade
        bucket = self.dicionario[r]  # encontrar o ponteiro pro bucket
        kkj = kj >> d  # retiro os bits de indexação para usar o restante para fazer hash no bucket
        kkjj = kkj
        achou = True
        final = False
        while (bucket._tabela[kkjj] == None or bucket._tabela[kkjj]._chave != k) and not final:
            kkjj += 1
            if kkjj == self._tambucket:
                kkjj = 0
                while bucket._tabela[kkjj] == None or bucket._tabela[kkjj]._chave != k:
                    kkjj += 1
                    if kkjj == kkj or kkjj == self._tambucket:
                        ## Não achou nada
                        achou = False
                        final = True
                        break
                    else:
                        ## Achou
                        bucket._tabela[kkjj] = None
                        achou = True
                        final = True
                        break
        if achou:
            bucket._tabela[kkjj] = None
            return True
        else:
            return False

    def setitem(self, k, num):
        kj = self._funcao_hash(k)  # hash
        d = self.profundidade()  # profundidade em bits
        r = kj & pow(2, d) - 1  # reduzindo a chave ao numero bits da profundidade
        bucket = self.dicionario[r]  # encontrar o ponteiro pro bucket
        kkj = kj >> d  # retiro os bits de indexação para usar o restante para fazer hash no bucket

        # de posse de bucket vamos preenche-lo
        elemento = self._Elemento(k, num)
        kkjj = kkj
        if bucket._tabela[kkjj] == None:
            bucket._tabela[kkjj] = elemento
            hashCheio = False
        else:
            while kkjj < self._tambucket and bucket._tabela[kkjj] != None:
                kkjj += 1
            if kkjj == self._tambucket:  ## chegou ao final do bucket
                kkjj = 0  ## circulando
                while kkjj < kkj and bucket._tabela[kkjj] != None:
                    kkjj += 1
                if kkjj == kkj or kkjj == self._tambucket:  ## Hash cheio
                    hashCheio = True
                else:  ## encontrou uma vaga
                    bucket._tabela[kkjj] = elemento
                    hashCheio = False
            else:
                bucket._tabela[kkjj] = elemento
                hashCheio = False
        if hashCheio:
            self.dicionario = self.ampliadict()  ## Ampliar 1 bit no dictionary
            return False
        else:
            return True

if __name__ == '__main__':

    b = int(input("Entre com o tamanho de cada bucket: "))

    # A Hash terá a metade do numero de chaves
    myHashTable = HashTable(int(b))

    print("Incluindo alguns elementos")
    print("=========================")
    for i in range(1, 9):
        myHashTable.setitem(i, randint(1, 1000))
        myHashTable.print()

    print("Excluindo alguns elementos")
    print("=========================")
    for i in range(1, 10, 3):
        myHashTable.delitem(i)
        myHashTable.print()
