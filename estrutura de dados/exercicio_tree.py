class Node:
    def __init__(self, data, right, left):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = Node(None, None, None)
        self.root = None

    def inserir(self, valor):
        novo = Node(valor, None, None)
        if self.root == None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if valor <= atual.data: #ir para esquerda
                    atual = atual.left
                    if atual == None:
                        anterior.left = novo
                        return #fim da condição que coloca dado a esquerda
                else: #inicio de cond para direita caso valor ser maior que o nó
                    atual = atual.right
                    if atual == None:
                        anterior.right = novo
                        return
                    #fim da condição folha direita

    def buscar(self, valor):
        if self.root == None:
            return None
        atual = self.root
        while atual.data != valor:
            if valor < atual.data:
                atual = atual.left
            else:
                atual = atual.right
            if atual == None:
                return None
        return atual

    def noSucessor(self, apaga):
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.right
        while atual != None:
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.left

        if sucessor != apaga.right:
            paidosucessor.left = sucessor.right
            sucessor.right = apaga.left

        return sucessor





    def printVal(self):
        print(f'esquerda: {self.root.left}')
        print(f'Raiz:{self.root}')
        print(f'direita: {self.root.right}')

