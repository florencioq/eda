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

    def _bit2letras(self):
        letras = []
        for b in bits(self._bits):
            letras.append(self._letras[int(log(b, 2))])
        return letras

    def add(self, caractere):
        self._bits = caractere
        self._bit2letras()

    def print(self):
        print(self._bit2letras())


if __name__ == '__main__':
    mySet = Set()
    mySet.add(12)
    mySet.print()
