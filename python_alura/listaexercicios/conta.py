
class Conta:
    def __init__(self, num, nome, saldo=0):
        self._numero = num
        self._nome = nome
        self._saldo = saldo

    def alterarNome(self, nome):
        self._nome = nome

    def deposito(self,valor):
        self._saldo += valor
        return self._saldo

    def saque(self,valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            return f'Saldo insuficiente!'
        return self._saldo

    def __repr__(self):
        return f' Conta: {self._numero}\n Titular: {self._nome}\n Saldo: {self._saldo}'