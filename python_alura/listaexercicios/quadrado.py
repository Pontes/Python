
class Quadrado:
    def __init__(self, tamanho):
        self.tamanhoLado = tamanho

    def setNovoTamanho(self, valor):
        self.tamanhoLado = valor

    def getTamanhoLado(self):
        return self.tamanhoLado

    def calcularArea(self):
        return self.tamanhoLado**2
