from random import *

class Heap():

    ## Classe dos itens que ficarão no Heap
    class Elemento:

        def __init__(self, chave, valor, indice):
            self._chave = chave
            self._valor = valor
            self._indice = indice

    def __init__(self):
        self._dados = []

    def vazio(self):
        return len(self._dados) == 0

    ## Partindo de uma posição j retorna a posição do pai de j
    def _pai(self, j):
        return (j - 1) // 2

    ## Partindo de uma posição j retorna a posição do filho à esquerda de j
    def _esquerda(self, j):
        return 2 * j + 1

    ## Partindo de uma posição j retorna a posição do filho à direita de j
    def _direita(self, j):
        return 2 * j + 2

    def tamanho(self):
        return len(self._dados)

    def add(self, chave, valor):
        elemento = self.Elemento(chave, valor, len(self._dados))
        self._dados.append(elemento)
        self._sobeheap(len(self._dados) - 1)
        return elemento

    def _sobeheap(self, j):
        pai = self._pai(j)
        if j > 0 and self._dados[j]._chave < self._dados[pai]._chave:
            self._troca(j, pai)
            self._sobeheap(pai)

    def _troca(self, i, j):
        self._dados[i], self._dados[j] = self._dados[j], self._dados[i]
        self._dados[i]._indice = i
        self._dados[j]._indice = j

    def _ajusta(self, j):
        if j > 0 and self._dados[j]._chave < self._dados[self._pai(j)]._chave:
            ## Se o elemento que caiu de para-quedas é menor que o pai
            ## Basta subir com ele
            self._sobeheap(j)
        else:
            ## Caso contrário basta baixa-lo
            self._baixaheap(j)

    def printHeap(self):
        for i in self._dados:
            print(i._chave, i._valor, i._indice)

    def _baixaheap(self, j):
        if self._temesquerda(j):  # se não existe elemento à esquerda, não precisa fazer nada
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
            self._troca(0, len(self._dados) - 1)
            retorno = self._dados.pop()
            self._baixaheap(0)
            return (retorno._chave, retorno._valor)

    def recupera_linear(self, chave):
        for i in self._dados:
            if i._chave == chave:
                return i
        return None

    ## Isso é para testar se o vetor ainda é um HEAP
    def eheap(self):
        return all(self._dados[i]._chave >= self._dados[(i - 1) // 2]._chave for i in range(1, len(self._dados)))

    def remove(self, elemento):
        indice = elemento._indice
        if indice == self.tamanho()-1: # se for o último, deleta
            self._dados.pop()
        else: # não é o último
            self._troca(indice, self.tamanho()-1)  ## poe ele pro final
            self._dados.pop() ## remove o cara
            self._ajusta(indice)
        return (elemento._chave, elemento._valor)

    def libera(self):
        self._dados = None

    def update(self, elemento, novachave, novovalor):
        indice = elemento._indice
        elemento._chave = novachave
        elemento._valor = novovalor
        self._ajusta(indice)

if __name__ == '__main__':
    myHeap = Heap()
    myHeap.printHeap()
    n = 1
    ## Inserindo itens
    print("Inserindo elementos")
    print("-------------------")
    for i in range(10 * n, 0, -1):
        myHeap.add(randint(1, 100), randint(1, 100))
        myHeap.printHeap()
        print(myHeap.eheap())
        print("------------------")
    ## Removendo pela cabeça
    print("Removendo elementos pela cabeça")
    print("-------------------")
    for i in range(n):
        myHeap.remove_minimo()
        myHeap.printHeap()
        print(myHeap.eheap())
        print("------------------")
    print(myHeap.eheap())
    print("Recuperando alguns elementos pela Chave")
    for i in range(50):
        e = myHeap.recupera_linear(i)
        if e != None:
            print(e._chave, e._valor)
    print(myHeap.eheap())
    ## Incluindo e removendo itens aleatoriamente
    print("Inserindo,recuperando e removendo elementos")
    print("-------------------------------")
    for i in range(5 * n):
        elemento = myHeap.add(randint(1, 100), randint(1, 100))
        print("Inserindo Elemento: " + str(elemento._chave))
        myHeap.printHeap()
        print(myHeap.eheap())
        print("------------------")
        print("Removendo Elemento: " + str(elemento._chave))
        myHeap.remove(elemento)
        myHeap.printHeap()
        print(myHeap.eheap())
        print("------------------")
    print(myHeap.eheap())
    print("Alterando elementos")
    for i in range(5 * n):
        elemento = myHeap.add(randint(1, 100), randint(1, 100))
        print("Inserindo Elemento: " + str(elemento._chave))
        myHeap.printHeap()
        print(myHeap.eheap())
        print("------------------")
        print("Alterando Elemento: " + str(elemento._chave))
        novachave = randint(1, 100)
        novovalor = randint(1, 100)
        print("Novo Elemento: " + str(novachave))
        myHeap.update(elemento, novachave, novovalor)
        myHeap.printHeap()
        print(myHeap.eheap())
        print("------------------")
    print("É um heap?")
    print(myHeap.eheap())
    print("Liberando memória")
    myHeap.libera()
    del myHeap
