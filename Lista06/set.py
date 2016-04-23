from math import *
from string import *

## There's a trick for just getting the 1's out of the binary representation without having to iterate over all the intervening 0's:
## http://stackoverflow.com/questions/8898807/pythonic-way-to-iterate-over-bits-of-integer
def bits(n):
    while n:
        b = n & (~n + 1)
        yield b
        n ^= b

class Set():
    def __init__(self):
        self._letras = ''
        self._bits = 0

    ## Converte numero em letras
    def _bit2letras(self):
        letras = []
        for b in bits(self._bits):
            logb = int(log(b, 2))
            letras.append(self._letras[logb])
        return letras

    ## Adiciona um elemento ao conjunto
    def add(self, caractere):
        self._bits = caractere
        self._bit2letras()

    ## Printa o conjunto
    def printConjunto(self):
        print(self._bit2letras())

    def printUniverso(self):
        print('Universo: ' + self._letras)

    def getUniverso(self):
        return self._letras

    ## Seta o Universo dos conjunto
    def setUniverso(self, universo):
        universo = ''.join(set(universo))  ## remove duplicados
        self._letras = ''.join(sorted(universo))  ## ordena

    def uniao(self, conjunto):
        ## So tem sentido se os universos forem os mesmos
        if self._letras == conjunto._letras:
            self._bits = self._bits | conjunto._bits
        else:
            raise ("Universos diferentes")

    def igual(self, conjunto):
        ## So tem sentido se os universos forem os mesmos
        if self._letras == conjunto._letras:
            if self._bits == conjunto._bits:
                return True
            else:
                return False
        else:
            raise ("Universos diferentes")

    def intersecao(self, conjunto):
        ## So tem sentido se os universos forem os mesmos
        if self._letras == conjunto._letras:
            self._bits = self._bits & conjunto._bits
        else:
            raise ("Universos diferentes")

    def diferenca(self, conjunto):
        ## So tem sentido se os universos forem os mesmos
        if self._letras == conjunto._letras:
            self._bits = self._bits - (self._bits & conjunto._bits)
        else:
            raise ("Universos diferentes")

    def subconjunto(self, conjunto):
        ## So tem sentido se os universos forem os mesmos
        if self._letras == conjunto._letras:
            if self._bits & conjunto._bits == conjunto._bits:
                return True
            else:
                return False
        else:
            raise ("Universos diferentes")

    def delElementos(self, conjunto):
        numeros = 0
        for letra in conjunto:
            posicao = self._letras.find(letra)
            if posicao != -1:
                numeros = int(pow(2, posicao))
                numeros = ~numeros
                self._bits = self._bits & int(numeros)

    def setElementos(self, conjunto):
        numeros = 0
        self._bits = 0  # limpa
        for letra in conjunto:
            posicao = self._letras.find(letra)
            if posicao != -1:
                numeros = pow(2, posicao)
                self._bits = self._bits | int(numeros)

    def complemento(self):
        univ = Set()
        univ.setUniverso(self.getUniverso())
        univ.setElementos(self.getUniverso())
        univ.diferenca(self)
        letras = univ._bit2letras()
        return letras

    ## Seta o conjunto de dados
    def addElementos(self, conjunto):
        numeros = 0
        for letra in conjunto:
            posicao = self._letras.find(letra)
            if posicao != -1:
                numeros = pow(2, posicao)
                self._bits = self._bits | int(numeros)

if __name__ == '__main__':
    print("Criando o conjunto")
    mySet1 = Set()
    print("Seu universo será tudo o que for printável; pode ser outro se quizer")
    mySet1.setUniverso(printable)
    print("Printando o Universo")
    mySet1.printUniverso()
    print("Acrescentando alguns elementos: jose florencio")
    mySet1.addElementos('jose florencio')
    mySet1.printConjunto()
    mySet2 = Set()
    mySet2.setUniverso(mySet1.getUniverso())
    mySet2.addElementos('de queiroz neto')
    print("=============================================")
    print("União de conjuntos")
    print("--------------------")
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Conjunto 2")
    mySet2.printConjunto()
    print("Resultado")
    mySet1.uniao(mySet2)
    mySet1.printConjunto()
    print("=============================================")
    print("Remoção de elementos")
    print("--------------------")
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Removendo: queiroz")
    mySet1.delElementos('queiroz')
    print("Resultado")
    mySet1.printConjunto()
    print("=============================================")
    print("Interseção de conjuntos")
    print("-----------------------")
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Conjunto 2")
    mySet2.printConjunto()
    mySet1.intersecao(mySet2)
    print("Resultado")
    mySet1.printConjunto()
    print("=============================================")
    print("Diferença de conjuntos")
    print("-----------------------")
    mySet1.addElementos('florencio')
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Conjunto 2")
    mySet2.printConjunto()
    print("Conjunto 1 - Conjunto 2 =")
    mySet1.diferenca(mySet2)
    mySet1.printConjunto()
    print("=============================================")
    print("Verificar se é subconjunto")
    print("-----------------------")
    mySet1.addElementos('florencio')
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Conjunto 2")
    mySet2.printConjunto()
    print("Conjunto 2 é subconjunto de Conjunto 1?")
    print(mySet1.subconjunto(mySet2))
    mySet2.delElementos('florencio de queiroz neto')
    mySet2.addElementos('rencio')
    print("Conjunto 2")
    mySet2.printConjunto()
    print("Conjunto 2 é subconjunto de Conjunto 1?")
    print(mySet1.subconjunto(mySet2))
    print("=============================================")
    print("Verificar igualdade de conjuntos")
    print("-----------------------")
    mySet1.addElementos('florencio')
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Conjunto 2")
    mySet2.printConjunto()
    print("Conjunto 1 é igual ao Conjunto 2?")
    print(mySet1.igual(mySet2))
    mySet2.setElementos('florencio')
    print("Conjunto 2")
    mySet2.printConjunto()
    print("Conjunto 1 é igual ao Conjunto 2?")
    print(mySet1.igual(mySet2))
    print("=============================================")
    print("Gerar o complemento de um conjunto")
    print("-----------------------")
    mySet1.setUniverso('abcdefgh')
    mySet1.printUniverso()
    mySet1.setElementos('qazwsxedc')
    print("Conjunto 1")
    mySet1.printConjunto()
    print("Print complemento de Conjunto 1")
    print(mySet1.complemento())
