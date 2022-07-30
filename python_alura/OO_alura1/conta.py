
class Conta:
    # o init é uma função que inicializa o python em java seria uma função construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objetos {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar__(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        saldo_disponivel = self.__saldo + self.__limite

        if self.__pode_sacar__(valor):
            self.__saldo -= valor
        else:
            print(f'Valor indisponível: {valor}.')
            print(f'Valor disponivel para saque: R$ {saldo_disponivel}')

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)
        self.extrato()
        print(f'Tranferencia de R$ {valor} para {destino}')

    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    ## metodo da classes sem ter referencia, método estatico (method static)
    ## não passa o proprio objeto
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa': '104','Bradesco':'237'}

