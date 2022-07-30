
class Data:
    def __init__(self,d,m,a):
        self.dia = d
        self.mes = m
        self.ano = a

    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
