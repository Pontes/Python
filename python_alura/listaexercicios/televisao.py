class Televisao:

    def __init__(self):
        self._canal = 0
        self._volume = 0

    def mudarCanal(self,valor):
        if valor >= 0 and  valor <= 100:
            self._canal = valor
            return f'Canal {self._canal}'
        return f'Canal {valor} não Existe'

    def aumentarVol(self):
        if self._volume >= 0 and self._volume < 100:
            self._volume += 1
            return f' Volume: {self._volume}'
        return f'Volume {self._volume}'

    def diminuirVol(self):
        if self._volume > 0 and self._volume <= 100:
            self._volume -= 1
            return f' Volume: {self._volume}'
        return f'Volume {self._volume}'
