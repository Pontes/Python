
class Tv:

    def __init__(self):
        self._canal = [100,101,102,103,104,105]
        self._volume = [0,10,20,30,40,50,60,70,80,90,100]

    def mudarCanal(self, valor):
        for x in self._canal:
            if x == valor:
                return f'Canal {x}'

        return f'O Canal: {valor} não existe!'

    def aumentarVol(self,valor):
        for x in self._volume:
            if x == valor:
                return f'Volume em {x}'

    def diminuirvol(self,valor):
        for x in self._volume:
            if x == valor:
                return f'Volume em {x}'