"""_summary_
Trabalho Laboratório de interface - Universidade de Vassouras
@author: Pontes Junior
"""

class Agenda:
    def __init__(self, nome, tel):
        self.nome =  nome
        self.tel = tel


    
    def arquivoPadrao(self):
        nomeArquivo = "agenda_py.txt"
        return nomeArquivo

    
    def salvarAgenda(self,agenda, nome, tel):
        agenda.write(nome.upper() + ", " + tel +"\n")
        agenda.close()
        return None

    
    def novoContato(self, agenda):
        self.nome = input("Digite o nome: ")
        self.tel = input("Digite o Telefone: ")
        x = self.abrirAgenda(self.arquivoPadrao(),'a')
        self.salvarAgenda(x, self.nome, self.tel)
        print("Contato Adicionado com sucesso!")
        
    
    def abrirAgenda(self, arq, modo):
        arquivo = open(arq, modo)
        return arquivo

class Contato(Agenda):
    def __init__(self):
        self.agenda = self.arquivoPadrao()

    
    def salveSe(self):
        pass

    
    def getContatos(self):
        arquivo = self.abrirAgenda(self.arquivoPadrao(),"r")
        dados = arquivo.readlines()
        arquivo.close()
        return dados
    
    
    def excluirContato(self):
        nome = input("Digite o nome para Excluir: ").upper()

        arqOriginal = self.getContatos()
        arqTemp = self.abrirAgenda('agendaTemp.txt','w')
        tam = len(arqOriginal)        

        for i in range(0,tam):
            arqTemp.write(arqOriginal[i])
        
        arqTemp.close()

        arqNovo = self.abrirAgenda(self.arquivoPadrao(),'w')
        arqTempAtual = self.abrirAgenda("agendaTemp.txt","r")
        dados = arqTempAtual.readlines()
        arqTempAtual.close()

        for i in range(0,tam):
            if nome in dados[i]:
                pass
            else:
                arqNovo.write(dados[i])
        
        arqNovo.close()


    def consultarNome(self):
        nome = input("Digite o nome para consultar: ").upper()
        dados = self.getContatos()
        tam = len(dados)
    
        for i in range(0,tam): 
            if nome in dados[i]:
                nome, tel = dados[i].split(',')
                self.imprimirContato(nome, tel)
                break
            if i >= (tam-1):
                self.imprimirSemContato()                             
    
    
    def listarContatos(self):
        dados = self.getContatos()
        tam = len(dados)
        print("\n")
        print("#------- Listagem de Contatos ------- #")
        for i in range(0,tam): 
            nome, tel = dados[i].split(',')
            self.imprimirListaContato(nome, tel)           
        

    def imprimirContato(self,contato, tel):
        print("\n")
        print("#------- NOME ENCONTRADO ------- #")
        print(f'Nome: {contato}')
        print(f'Telefone: {tel}')
        print("#------- NOME ENCONTRADO ------- #")
        print("\n")

    
    def imprimirListaContato(self,contato, tel):
        print(f'Nome: {contato}')
        print(f'Telefone: {tel}')        
        print("-"*50)

    
    def imprimirSemContato(self):
        print("\n")
        print("#------- NÃO FOI POSSÍVEL ENCONTRAR O NOME -------#")
        print("\n")

def menu():
    print('#-----------------------------------#')
    print('#             A G E N D A           #')
    print('#-----------------------------------#')
    print('#    OPÇÕES                         #')
    print('#    1 - CADASTRAR NOME             #')
    print('#    2 - CONSULTAR NOME             #')
    print('#    3 - EXCLUIR NOME               #')
    print('#    4 - LISTAR TODOS OS NOMES      #')
    print('#    5 - SAIR                       #')
    print('#-----------------------------------#')
    print("\n")

    agCont = Contato()
    op = int(input('Digite uma opção: '))

    if  op == 1:
        agCont.novoContato(agCont.agenda)
    elif op == 2:
        agCont.consultarNome()
    elif op == 3:
        agCont.excluirContato()
    elif op == 4:
        agCont.listarContatos()
    elif op == 5:
        print("saindo da agenda...")
        print("Agenda Finalizada")
        exit()
    else: 
        print("Opção Inválida! Digite a Opção Correta!")


def main():
    
    while True:
        menu()

main()
