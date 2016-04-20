from random import *

class Heap():

    class _Elemento:

        def __init__(self, chave, valor):
            self._chave = chave
            self._valor = valor

        def menor(self, outro):
            return self._chave < outro._chave

    def vazio(self):
        return len(self._dados) == 0

    def __init__(self):
        self._dados = []

    def _pai(self, j):
        return (j-1) // 2

    def _esquerda(self, j):
        return 2*j +1

    def _direita(self, j):
        return 2*j+2

    def tamanho(self):
        return len(self._dados)

    def add(self, chave, valor):
        self._dados.append(self._Elemento(chave, valor))
        self._sobeheap(len(self._dados)-1)

    def _sobeheap(self, j):
        pai = self._pai(j)
        if j > 0 and self._dados[j]._chave < self._dados[pai]._chave:
            self._troca(j, pai)
            self._sobeheap(pai)

    def _troca(self, i, j):
        self._dados[i], self._dados[j] = self._dados[j], self._dados[i]

    def printHeap(self):
        for i in self._dados:
            print(i._chave, i._valor)

    def _baixaheap(self, j):
        if self._temesquerda(j): # se não existe elemento à esquerda, não precisa fazer nada
            esquerda = self._esquerda(j)
            menor = esquerda
            if self._temdireita(j):
                direita = self._direita(j)
                if self._dados[direita]._chave < self._dados[esquerda]._chave:
                    menor = direita
            if self._dados[menor]._chave < self._dados[j]._chave:
                self._troca(j, menor)
                self._baixaheap(menor)

    def _temesquerda(self, j):
        ## Se o calculo der menor que o tamanho total, é porque o elemento existe.
        ## Se der maior, é que o elemento à esquerda daria fora do Heap
        return self._esquerda(j) < len(self._dados)

    def _temdireita(self, j):
        ## Se o calculo der menor que o tamanho total, é porque o elemento existe.
        ## Se der maior, é que o elemento à direita daria fora do Heap
        return self._direita(j) < len(self._dados)

    def remove_minimo(self):
        if self.vazio():
            return False
        else:
            self._troca(0, len(self._dados)-1)
            retorno = self._dados.pop()
            self._baixaheap(0)
            return (retorno._chave, retorno._valor)

if __name__ == '__main__':
    myHeap = Heap()
    myHeap.printHeap()

    ## Inserindo itens
    for i in range(6,0,-1):
        myHeap.add(i,randint(1,100))
        myHeap.printHeap()
        print("------------------")
    ## Removendo pela cabeça
    for i in range(6):
        myHeap.remove_minimo()
        myHeap.printHeap()
        print("------------------")

