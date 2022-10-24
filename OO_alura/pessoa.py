class Pessoa:
    tamanho_cpf = 11

    def __init__(self,cpf,nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False


pe = Pessoa('12345678911', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('123456789', 'Cristal')
print(pe.valida_cpf())

