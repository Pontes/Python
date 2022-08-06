from model import Questionario

class ViewQuestoes:
    def entradaDados(self):
        codigo = input("Digite um código para pergunta: ")
        categoria = input("Diga qual a categoria da pergunta: ")
        pergunta = input("Digite a sua pergunta: ")
        print("*********************************************")
        print("*** 1 - Improvável         ***")
        print("*** 2 - Pouco provável     ***")
        print("*** 3 - Um Pouco provável  ***")
        print("*** 4 - Provável           ***")
        print("*** 5 - Muito Provável     ***")
        resposta = int(input("Digite o número da resposta: "))
        print("")
        dados_inseridos = Questionario(pergunta, resposta, categoria, codigo)
        return dados_inseridos

    def mostraOpcao(self):
        ("****************************************************")
        print("*** Escolha uma das opções ***")
        print("Digite 1 para adicionar uma pergunta")
        print("Digite 2 para finalizar o questionário")
        print("****************************************************")
        opcao = input(" Opção: ")
        return opcao

    def mostrarPerguntas(self, lista):
        for q in lista:
            print(f'{q._codigo_} - {q._categoria_} : Pergunta: {q._pergunta_}')
            if q._resposta_ == 1:
                print("*** 1 - Improvável         ***")
            elif q._resposta_ == 2:
                print("*** 2 - Pouco provável     ***")
            elif q._resposta_ == 3:
                print("*** 3 - Um Pouco provável  ***")
            elif q._resposta_ == 4:
                print("*** 4 - Provável           ***")
            else:
                print("*** 5 - Muito Provável     ***")

            print("****************************************************")


