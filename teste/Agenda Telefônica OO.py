class Agenda: 
    def __init__(self) -> None:
        self.listaContatos = []
            
    def novoContato(self): 
        print('='*50)
        nome = input('Digite o nome: ')
        sobrenome = input('Digite o sobrenome: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        print('='*50)
        
        #lista
        self.listaContatos.append(Contato(nome,sobrenome,telefone,email))    

    def salvarAgenda():
        pass

    def abrirAgenda(self):
        print('='*50)
        print(' '*20, 'Contatos:') 
        #Lista
                
        for i in self.listaContatos:
            print(f'\n Nome:{i.nome}',f'\n Sobrenome: {i.sobrenome}', f'\n Telefone: {i.telefone}', f'\n Email:{i.email}')
        print('='*50)
           
class Contato: 
    def __init__(self, nome, sobrenome, telefone, email) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email

    def salveSe(self):
        #(9xxxx-xxxx)
        if len(self.telefone) == 9:
            return True 
      
def menu():
    agenda = Agenda()
    while True:
       print('='*50)
       print('1 - Adicionar')
       print('2 - Mostrar')
       print('0 - Sair')
       print('='*50)
       pick = int(input('Entre com a opção: '))
       if pick == 1:
           agenda.novoContato()
       elif pick == 2:
           agenda.abrirAgenda()
       elif pick == 0:
            break
       else:
           print('Nenhuma opção selecionada')   

menu()
    
    