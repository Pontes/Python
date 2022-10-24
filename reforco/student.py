class Student():
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibirEstudante(self):
        print(f'Nome: {self.nome}, idade {self.idade}, email:{self.email}')

aluno1 = Student('Pontes', 43, 'pontes@pontesti.com.br')
aluno1.exibirEstudante()