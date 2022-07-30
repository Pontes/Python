class Macaco:
    def __init__(self, nome):
        self._nome = nome
        self._bucho = []

    def comer(self, comida):
        self._bucho.append(comida)

    def verBucho(self):
        print("No Bucho do ", self._nome,"->", self._bucho)

    def digerir(self):
        if(len(self._bucho) > 0):
            self._bucho.pop(0)

    def __repr__(self):
        return f'{self._nome}'


m1 = Macaco("ximpa")
m2 = Macaco("panze")

m1.comer("maça")
m1.verBucho()

m1.comer("banana")
m1.verBucho()

m1.comer("abacaxi")
m1.verBucho()
m1.digerir()
m1.verBucho()

m2.comer("maça")
m2.comer("banana")
m2.comer(m1)
m2.verBucho()


