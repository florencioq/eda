# 2) No encadeamento interior, em que as chaves são armazenadas na própria tabela de hash, forneça
# um exemplo em que duas chaves distintas, x e y, com h(x)≠ h(y) podem apresentar colisões.
# Exemplifique com uma tabela hash de 11 elementos. Defina uma função de hash para tornar sua
# explicação mais concreta.

# Resposta: O problema pode ocorrer na Variante 2 do encadeamento interior, quando se usa *todo* o espaço de
# endereçamento. Neste caso, uma colisão anterior pode provocar a ocupação de um endereço, que seria para
# outra chave. Quando uma chave justa fosse ser alocada, este local já estaria ocupado por causa de uma
# colisão anterior. Neste caso temos uma colisão secundária.

# No programa abaixo, a chave 1 ocupa a posição 5. Em seguida, a chave 6 também vai até a posição 5, que já está
# ocupada. Pelo ancadeamento interior, a chave 6 vai ser alocada na posição 7 pois a posição 6 já está ocupada
# pela chave justa 4.
# A colisão secundária ocorre então quando a chave 7, que deveria ser justamente alocada na posição 7, já encontra
#  esta posição ocupada pela chave 6, em virtude de uma colisão anterior

# Exemplo:
# Chave-Posição
# 0-3
# 1-5 ----------> Ocupa a posição 5.
# 2-2
# 3-4
# 4-6
# 5-8
# 6-5 ----------> Colisão. Chave 6 segue para próxima vaga: posição 7.
# 7-7 ----------> Colisão sedundária pois a posição 7 já está ocupada em virtude de colisão anterior.
# 8-9
# 9-6
# 10-8
# 11-10

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