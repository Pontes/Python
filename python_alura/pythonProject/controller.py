from view import ViewQuestoes
from model import Questionario

class Controller:
    _listaQuestoes_ = []

    def executar(self):
        perguntas = ViewQuestoes()
        op = perguntas.mostraOpcao()

        while op =='1':
            p = perguntas.entradaDados()
            self._listaQuestoes_.append(p)
            op = perguntas.mostraOpcao()

        perguntas.mostrarPerguntas(self._listaQuestoes_)


