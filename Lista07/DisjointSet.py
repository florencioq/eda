class DisjointSet():

    def __init__(self):
        self._conjunto = {}

    def makeset(self, valor):
        self._conjunto[valor] = valor

    def print(self):
        print(self._conjunto)

    def find(self, valor):
        return self._conjunto[valor]

    def mesmo(self, e1, e2):
        if self._conjunto[e1] == self._conjunto[e2]:
            return True
        else:
            return False

    # União E une dois conjuntos baseando-se nos elementos
    def uniaoE(self, e1, e2):
        """
        e1: primeiro elemento cujo rep será o final da uniao
        e2: segundo elemento
        retorna True se tem algum elemento e1. Faz a união se houver o elemento e2.
        retorna False se não há elemento e1 e não faz a união
        """
        r1 = self._conjunto[e1]
        r2 = self._conjunto[e2]
        return self.uniaoR(r1, r2)

    # União R une dois conjuntos baseando-se nos representantes
    def uniaoR(self, r1, r2):
        """
        r1: primeiro representante e final da uniao
        r2: segundo representante
        retorna True se tem algum elemento com representante r1. Faz a união se houver elementos com representante r2.
        retorna False se não há elementos com representante r1 e não faz a união
        """
        for key1, value1 in self._conjunto.items():
            if self._conjunto[key1] == r1:
                for key2, value2 in self._conjunto.items():
                    if self._conjunto[key2] == r2:
                        self._conjunto[key2] = value1
                return True
        return False

if __name__ == '__main__':
    print("Criando o conjunto com subconjuntos disjuntos")
    myDS = DisjointSet()
    print("Criando uns subconjuntos")
    for i in range(5):
        myDS.makeset(i)
    print("Printando os conjuntos")
    myDS.print()
    print("Unindo R conjuntos 1 e 2")
    myDS.uniaoR(1, 2)
    myDS.print()
    print("Unindo R conjuntos 1 e 3")
    myDS.uniaoR(1, 3)
    myDS.print()
    print("Unindo R conjuntos 0 e 1")
    myDS.uniaoR(0, 1)
    myDS.print()
    print("Retornando o representante dos elementos")
    for i in range(5):
        print(str(i) + "-->" + str(myDS.find(i)))
    print("Verificando se 1 e 2 fazem parte do mesmo conjunto")
    print(myDS.mesmo(1, 2))
    print("Verificando se 1 e 4 fazem parte do mesmo conjunto")
    print(myDS.mesmo(1, 4))
    print("União E de 1 e 4")
    myDS.print()
    myDS.uniaoE(1, 4)
    myDS.print()
