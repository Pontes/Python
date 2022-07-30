class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo é {}".format(self.saldo))

    def deposita(self, v):
        self.saldo += v
        print("Seu saldo agora é de: R${}".format(self.saldo))

    def saca(self,v):
        self.saldo -= v
        print("Seu saldo agora é de: R${}".format(self.saldo))
