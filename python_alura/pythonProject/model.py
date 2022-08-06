class Questionario:
    _questao_ = []
    _pergunta_ = ""
    _resposta_ = 0
    _categoria_ = ""
    _codigo_ = ""

    def __init__(self, p, r, c, cod):
        self._pergunta_ = p
        self._resposta_ = r
        self._categoria_ = c
        self._codigo_ = cod
