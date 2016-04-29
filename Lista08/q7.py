from random import *
from string import *

def hash1(x, tam):
    return x % tam

for i in [4,10,24,36,25,14,23,100,2,3,12,13]:
    chave = i
    print (str(chave)+"-"+str(hash1(chave,12))+"-"+str(hash1(chave+2,12))+"-"+str(hash1(chave+4,12))+"-"+str(hash1(chave+6,12))+"-"+str(hash1(chave+8,12))+"-"+str(hash1(chave+10,12)))