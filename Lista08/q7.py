from random import *
from string import *

def hash1(x, tam):
    return x % tam


for i in [19, 38, 64, 100, 81, 47, 27, 31]:
    chave = i
    tam = 17
    print(str(chave) + "-" + str(hash1(chave, tam)) + "-" + str(hash1(chave + 1, tam)) + "-" + str(
        hash1(chave + 2, tam)) + "-" + str(hash1(chave + 3, tam)) + "-" + str(hash1(chave + 4, tam)) + "-" + str(
        hash1(chave + 5, tam)))
