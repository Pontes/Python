class Funcionario:
    prefixo = "Instrutor"

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'

c = Funcionario()

print(c.info())