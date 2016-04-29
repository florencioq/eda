# 2) Mostre, através de um desenho, como ficaria a tabela hash de 7 elementos que recebesse as
# seguintes chaves de busca 7,10,15,14,17,16 (nesta ordem).

# a) Se ela fosse com encadeamento exterior com a função de dispersão: ℎ(x) = (13 ∗ x ) % 7

# b) Se ela fosse com encadeamento aberto e com segunda função de dispersão: ℎ(x,j) = (13x+ 5j)%7, j=0,1,2,3,...

from random import *
from string import *

def hash1(x, tam, vez):
    return (13 * x + 5 * vez) % tam

for i in [7,10,15,14,17,16]:
    chave = i
    print (str(chave)+"-"+str(hash1(chave,7,0))+"-"+str(hash1(chave,7,1))+"-"+str(hash1(chave,7,2)))