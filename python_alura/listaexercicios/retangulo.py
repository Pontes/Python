class Retangulo:

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def setBase(self,base):
        self._base = base

    def setAltura(self, altura):
        self._altura = altura

    def getMedidas(self):
        return f'{self._base},{self._altura}'

    def calcularArea(self):
        return self._base * self._altura

    def calcularPerimetro(self):
        return 2 * self.calcularArea()



