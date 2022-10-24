class Jogo:

    def __init__(self, nome, vezes_jogo):
        self.__nome = nome
        self.__vezes_jogo = vezes_jogo

    @property
    def vezes_jogo(self):
        return self.__vezes_jogo

    @vezes_jogo.setter
    def vezes_jogo(self,vezes_jogo):
        self.__vezes_jogo = vezes_jogo