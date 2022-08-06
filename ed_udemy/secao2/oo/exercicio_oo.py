class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def media(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostraDados(self):
        return f'Nome: {self.nome}, nota 1:{self.nota1}, nota 2: {self.nota2}'

    def resultado(self):
        if self.media() >= 6.0:
            return "Aluno APROVADO"
        else:
            return "Aluno REPROVADO"


a1 = Aluno("Pontes", 10, 9)
a2 = Aluno("José", 4.5, 5.5)

print(a1.mostraDados())
print(f'Media do aluno: {a1.media()}')
print(f'O aluno está: {a1.resultado()}\n')
print('-'*50)
print(a2.mostraDados())
print(f'Media do aluno: {a2.media()}')
print(f'O aluno está: {a2.resultado()}\n')
print('-'*50)
