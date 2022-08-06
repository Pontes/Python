class Conta2:
    def __init__(self,numero,titular, saldo,limite):
        print("Construindo objeto{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        self.__imprimeLinha()
        print(f'Titular da conta: {self.__titular.title()}')
        print(f'Saldo atual: {self.__saldo} ')
        print(f'')
        self.__imprimeLinhas()

    def __imprimeLinha(self):
        print('-------------------------------------------------------')

    def __imprimeLinhas(self):
        print('=======================================================')

    def depositar(self, valor):
        self.__saldo += valor
        self.__imprimeLinha()
        print(f'Deposito realizado para {self.__titular}')
        print(f'No valor de: R$ {valor}')
        self.__imprimeLinhas()

    def __pode_sacar(self, valor_sacar):
        valor_disponivel_sacar =  self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel_sacar

    def sacar(self, valor):
        saldo_disponivel = self.__saldo + self.__limite

        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'Saque efetuado no valor de R$ {valor}')
            self.extrato()
        else:
            self.__imprimeLinha()
            print(f'Valor Indisponivel: R$ {valor}')
            print(f'Valor permitido para saque é de R$ {saldo_disponivel}')
            self.__imprimeLinhas()

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f'tranferencia realizada R$ {valor} para {destino}-{self.__titular}')

    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = limite













































