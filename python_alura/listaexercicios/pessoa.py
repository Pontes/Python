class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def envelhecer(self, idade):
        self._idade += idade
        if self._idade < 21:
            self.crescer(0.05)
        return f'{self._nome} tem {self._idade} anos'

    def engordar(self, peso):
        self._peso += peso
        return f'{self._nome} engordou, seu peso é {self._peso}'

    def emagrecer(self, peso):
        self._peso -= peso
        return f'{self._nome} emagreceu, seu peso é {self._peso}'

    def crescer(self, valor):
        self._altura += valor
        return f'{self._nome} sua altura é: {self._altura}'
