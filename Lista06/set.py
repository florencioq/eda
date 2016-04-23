from math import *

## There's a trick for just getting the 1's out of the binary representation without having to iterate over all the intervening 0's:
## http://stackoverflow.com/questions/8898807/pythonic-way-to-iterate-over-bits-of-integer
def bits(n):
    while n:
        b = n & (~n + 1)
        yield b
        n ^= b

class Set():
    def __init__(self):
        self._letras = 'abcdefgh'
        self._bits = 0

    ## Converte numero em letras
    def _bit2letras(self):
        letras = []
        for b in bits(self._bits):
            letras.append(self._letras[int(log(b, 2))])
        return letras

    ## Adiciona um elemento ao conjunto
    def add(self, caractere):
        self._bits = caractere
        self._bit2letras()

    ## Printa o conjunto
    def print(self):
        print(self._bit2letras())

    ## Seta o Universo dos conjunto
    def setUniverso(self, universo):
        self._letras = universo

    ## Seta o conjunto de dados
    def addElementos(self, conjunto):
        numeros = 0
        for letra in conjunto:
            posicao = self._letras.find(letra)
            if posicao != -1:
                numeros += pow(2, posicao)
        self._bits = self._bits | int(numeros)

if __name__ == '__main__':
    mySet = Set()
    mySet.setUniverso('abcedfgh')
    mySet.addElementos('c')
    mySet.print()
    mySet.addElementos('f')
    mySet.print()
    mySet.addElementos('h')
    mySet.print()
