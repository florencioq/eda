# 2) Explique com base no seu exemplo anterior porque ao remover uma chave de uma tabela hash
# você não pode simplesmente apagar a entrada da tabela.

# Exemplo:
# Chave-Posição
# 0-3
# 1-5 ----------> Ocupa a posição 5.
# 2-2
# 3-4
# 4-6
# 5-8
# 6-5 ----------> Colisão. Chave 6 segue para próxima vaga: posição 7 (a 6 já está ocupada).
# 7-7 ----------> Colisão sedundária pois a posição 7 já está ocupada em virtude de colisão anterior. Vai para pos. 9.
# 8-9
# 9-6
# 10-8
# 11-10

# Resposta: Um elemento não pode ser simplesmente retirado porque ele pode ter participação em uma colisão anterior
# fazer parte do caminho até chegar ao elemento que está alocado fora de seu lugar esperado.
# Por exemplo, após inserir o elemento 6, que por causa da colisão vai para o local 7 em vez do 5, não podemos
# simplesmente remover o elemento 1 da posição 5, pois ficaria a vaga e quando alguém for questionar o elemento
# 6, a posição justa dele estaria livre, indicado que ele não está na tabela, o que não é verdade, pois ele está na
# posição 7.

from random import *
from string import *

def hash(k, tam, a, b, primo):
    return (k * a + b) % primo % tam

primo = 109345121
a = 76567576  ## primo > aleatorio > 0
b = 54564656  ## primo > aleatorio > 0
lista = [0]*11

for i in range(11):
    lista[i] = 0

for i in range(12):
    chave = i
    print (str(chave)+"-"+str(hash(chave, 11, a, b, primo)))
    lista[(hash(chave, 11, a, b, primo))] += 1

print(lista.count(0))
print(lista)