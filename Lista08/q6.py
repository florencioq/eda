from random import *
from string import *

def hash1(x, tam):
    return x % tam

for i in range(35+1):
    chave = i
    print (str(chave)+"-"+str(hash1(chave,35)))