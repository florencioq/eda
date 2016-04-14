from random import *

n=randint(2000000,2000000)
lado=randint(1,2) # 1 esquerdo 2 direito
print (n, lado)

andadas = 0
passo = 1
ponto = 0
sentido = 1

achado = 0

while achado == 0:
    # porta está à frente
    if n==0:
        andadas = 0
        achado = 1
        break
    while ponto != n or sentido != lado:
        if sentido != lado:
            andadas = andadas + passo
        else:
            ponto = ponto + 1
            while ponto <= passo:
                if ponto == n:
                    # encontrado à esquerda
                    achado = 1
                    break
                else:
                    ponto = ponto + 1
                    andadas = andadas + 1
        # não foi achado e troca de sentido
        if achado == 1:
            break
        if sentido == 1:
            sentido = 2
        else:
            sentido = 1
        # reajusta o passo com todas as andadas anteriores
        andadas = andadas + passo
        ponto = 0
        passo = andadas
print(achado, andadas)