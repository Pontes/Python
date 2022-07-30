class No:
    def __init__(self,key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq

class Tree:

    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self,v):
        novo = No(v,None, None) #cria um novo nó
        if self.root == None:
            self.root = novo
        else: #se não for a raiz
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item: #ir para a esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                    #fim da condição ir a esquerda
                else: #ir para direita
                    atual = atual.dir
                    if atual ==None:
                        anterior.dir = novo
                        return
                    #fim da condição ir para a direita

    def buscar(self, chave):
        if self. root == None:
            return None   # se arvore vazia
        atual = self.root #começa a procurar desde a raiz
        while atual.item != chave: #enquanto não encontrou
            if chave < atual.item:
                atual = atual.esq #caminha para esquerda
            else:
                atual = atual.dir #caminha para direita
            if atual == None:
                return None #encontrou uma folha > sai
        return atual #terminou o laço while e chegou aqui é porque encontro o item

    # o Sucessor é o nó mais a esquerda da subarvore a direita do no que
    def nosucessor(self, apaga): #O parametro é a referencia para o no que deseja
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir  #vai para a subarvore a direita

        while atual != None: #enquanto não chegar no Nó mais a esquerda
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq #caminha para a esquerda
            ###########
            #quando sair do while "sucessor" ser´ao nó mais a esquerda da subárvore a direita
            # "paidosucessor" será o pai de sucessor e "apaga" o n´que deverá ser eleminado
            ##############

        if sucessor != apaga.dir: #se o sucessor nã é o filho a direita do nó que
            paidosucessor.esq = sucessor.dir #pai herda os filhos do sucessor que
            # lembrando que o sucessor nunca poderá ter filhos a esquerda, pois
            #lembrando ...
            sucessor.dir = apaga.dir
        return sucessor

    def remover(self, v):
        if self.root == None:
            return False # se árvore estiver vazia
        atual = self.root
        pai = self.root
        filho_esq = True
        #************ Buscando o valor *****************
        while atual.item != v: #eqnaunto não encontrou
            pai = atual
            if v < atual.item: #caminha para esquerda
                atual = atual.esq
                filho_esq = True # é filho a esquerda? sim
            else: # caminha para direita
                atual = atual.dir
                filho_esq = False #é filho a esquerda ? Não
            if atual == None:
                return False #encontrou uma folha




















