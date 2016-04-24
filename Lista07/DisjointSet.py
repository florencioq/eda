class DisjointSet():
    # class Elemento():
    #
    #     def __init__(self):
    #         self._representante = None
    #         self._valor = None

    def __init__(self):
        self._conjunto = {}

    def makeset(self, valor):
        elemento = self.Elemento()
        elemento._valor = valor
        elemento._representante = elemento
        self._conjunto.append(elemento)

    def print(self):
        for elem in self._conjunto:
            print(str(elem._valor) + "-" + str(elem._representante._valor))

    def find(self, valor):
        for elem in self._conjunto:
            if elem._valor == valor:
                return elem._representante._valor
        return None

    def mesmo(self, e1, e2):
        if

    # União R une dois conjuntos baseando-se nos representantes
    def uniao(self, r1, r2):
        """
        r1: primeiro representante e final da uniao
        r2: segundo representante
        retorna True se tem algum elemento com representante r1. Faz a união se houver elementos com representante r2.
        retorna False se não há elementos com representante r1 e não faz a união
        """
        for elem1 in self._conjunto:
            if elem1._representante._valor == r1:
                for elem2 in self._conjunto:
                    if elem2._representante._valor == r2:
                        elem2._representante = elem1._representante
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
    print("Unindo conjuntos")
    myDS.uniao(1, 2)
    print("Printando os conjuntos")
    myDS.print()
    print("Printando os conjuntos")
    myDS.uniao(1, 3)
    myDS.print()
