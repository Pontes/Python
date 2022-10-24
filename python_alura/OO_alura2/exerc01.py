class Programa:

    def __init__(self, nome, ano):
        self._nome_ = nome.title()
        self._ano_ = ano
        self._likes_ =0

    @property
    def likes(self):
        return self._likes_

    def dar_likes(self):
        self._likes_ += 1

    @property
    def nome(self):
        return self._nome_

    @nome.setter
    def nome(self, nome):
        self._nome_ = nome

    def __str__(self):
        return f'Nome: {self.nome} likes: {self.likes}'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao}min - likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - likes: {self.likes}'


vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

listinha = [atlanta, vingadores]

for programa in listinha:
    print(programa)
