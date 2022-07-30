class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade

    def setNome(self, nome):
        self._nome = nome

    def setFome(self, fome):
        self._fome = fome

    def setSaude(self, saude):
        self._saude = saude

    def setIdade(self, idade):
        self._idade = idade

    def getNome(self):
        return self._nome

    def getFome(self):
        return self._fome

    def getSaude(self):
        return self._saude

    def getIdade(self):
        return self._idade

    def humor(self):
        return self.getFome() * self.getSaude()
