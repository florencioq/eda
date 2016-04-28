from random import *
from string import *


# Estrutura de dados avançada
# José Florencio de Queiroz Neto
#
# 1) Escreva uma função de dispersão (hash) que tenha como chave um string com os nomes de
# paises, de até 32 caracteres. A tabela hash deve ter 513 elementos.

def aleastring():
    return ''.join(choice(ascii_uppercase + digits) for _ in range(32))

def hash(palavra, tam, a, b, primo):
    total = 0
    for idx, letra in enumerate(palavra):
        valor = ord(letra)
        total = total + idx * valor
    return (total * a + b) % primo % tam
primo = 109345121
a = 76567576  ## primo > aleatorio > 0
b = 54564656  ## primo > aleatorio > 0
lista = [0]*513

for i in range(513):
    lista[i] = 0

for i in range(5130):
    pais = aleastring()
    lista[(hash(pais, 513, a, b, primo))] += 1

print(lista.count(0))
print(lista)
