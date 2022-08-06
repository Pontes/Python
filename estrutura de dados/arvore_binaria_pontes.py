class No:

     def __init__(self, key, dir, esq):
          self.item = key
          self.dir = dir
          self.esq = esq

class Tree:

     def __init__(self):
          self.root = No(None,None,None)
          self.root = None

     def inserir(self, v):

          novo = No(v,None,None) # cria um novo Nó
          if self.root == None:
               self.root = novo
          else: # se nao for a raiz
               atual = self.root
               while True:
                    anterior = atual
                    if v <= atual.item: # ir para esquerda
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return
                    # fim da condição ir a esquerda
                    else: # ir para direita
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return
                    # fim da condição ir a direita

     def buscar(self, chave):
         if self.root == None:
              return None # se arvore vazia
         atual = self.root # começa a procurar desde raiz
         while atual.item != chave: # enquanto nao encontrou
               if chave < atual.item:
                    atual = atual.esq # caminha para esquerda
               else:
                    atual = atual.dir # caminha para direita
               if atual == None:
                    return None # encontrou uma folha -> sai
         return atual  # terminou o laço while e chegou aqui é pq encontrou item

     def nosucessor(self, apaga): # O parametro é a referencia para o No que deseja-se apagar
          paidosucessor = apaga
          sucessor = apaga
          atual = apaga.dir # vai para a subarvore a direita

          while atual != None:
               paidosucessor = sucessor
               sucessor = atual
               atual = atual.esq # caminha para a esquerda

          if sucessor != apaga.dir:
               paidosucessor.esq = sucessor.dir
               sucessor.dir = apaga.dir
          return sucessor

     def remover(self, v):
         if self.root == None:
             return False
         atual = self.root
         pai = self.root
         filho_esq = True
         while atual.item != v:
             pai = atual
             if v < atual.item:
                 atual = atual.esq
                 filho_esq = True
             else:
                 atual = atual.dir
                 filho_esq = False
             if atual ==  None:
                return False

         if atual.esq == None and atual.dir == None:
             if atual == self.root:
                 self.root = None
             else:
                 if filho_esq:
                    pai.esq = None
                 else:
                    pai.dir = None
         elif atual.dir == None:
             if atual == self.root:
                 self.root = atual.esq
             else:
                 if filho_esq:
                     pai.esq = atual.esq
                 else:
                     pai.dir = atual.esq
         elif atual.esq == None:
             if atual == self.root:
                 self.root = atual.dir
             else:
                 if filho_esq:
                     pai.esq = atual.dir
                 else:
                     pai.dir = atual.dir
         else:
             sucessor = self.nosucessor(atual)
             if atual == self.root:
                 self.root = sucessor
             else:
                 if filho_esq:
                     pai.esq = sucessor
                 else:
                     pai.dir = sucessor
             sucessor.esq = atual.esq

         return True

     def inOrder(self, atual):
         if atual != None:
             self.inOrder(atual.esq)
             print(atual.item,end=" ")
             self.inOrder(atual.dir)

     def preOrder(self,atual):
         if atual != None:
             print(atual.item, end=" ")
             self.preOrder(atual.esq)
             self.preOrder(atual.dir)

     def posOrder(self, atual):
         if atual != None:
             self.posOrder(atual.esq)
             self.posOrder(atual.dir)
             print(atual.item, end=" ")

     def altura(self,atual):
         if atual == None or atual.esq == None and atual.dir == None:
             return 0
         else:
             if self.altura(atual.esq) > self.altura(atual.dir):
                 return 1 + self.altura(atual.esq)
             else:
                 return 1 + self.altura(atual.dir)

     def folhas(self, atual):
         if atual == None:
             return 0
         if atual.esq == None and atual.dir == None:
             return 1
         return self.folhas(atual.esq) + self.folhas(atual.dir)

     def contarNos(self, atual):
         if atual == None:
             return 0
         else:
             return 1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

     def minn(self):
         atual = self.root
         anterior = None
         while atual != None:
             anterior = atual
             atual = atual.esq
         return anterior

     def maxx(self):
         atual = self.root
         anterior = None
         while atual != None:
             anterior = atual
             atual = atual.dir
         return anterior

     def nivelAltura(self, valor):
         atual = self.root
         x = 1
         while atual.item != valor:
             if valor < atual.item:
                 atual = atual.esq
             else:
                 atual = atual.dir
             if atual == None:
                 return None
             x += 1
         return x

     def caminhar(self):
         print(" Exibindo em ordem: ", end=" ")
         self.inOrder(self.root)
         print("\n Exibindo em pos-ordem: ", end="")
         self.posOrder(self.root)
         print("\n Exibindo em pre-ordem: ", end=" ")
         self.preOrder(self.root)
         print("\n Altura da arvore: %d" %(self.altura(self.root)))
         print(" Quantidade de folhas: %d" %(self.folhas(self.root)))
         print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))
         if self.root != None:
             print("Valor mínimo: %d" %(self.minn().item) + " Altura: ", self.nivelAltura(self.minn().item))
             print("Valor maximo: %d" %(self.maxx().item) + " Altura: ", self.nivelAltura(self.maxx().item))

arv = Tree()
print("Programa Árvore Binária")
opcao = 0
while opcao != 5:
    print("******************************************************")
    print("Entre com a opção: ")
    print(" --- 1 : Inserir")
    print(" --- 2 : Excluir")
    print(" --- 3 : Pesquisar")
    print(" --- 4 : Exibir Árvore")
    print(" --- 5 : Sair do Programa")
    print("*****************************************************")
    opcao = int(input("->"))
    if opcao == 1:
        x = int(input("Informe o valor -> "))
        arv.inserir(x)
    elif opcao == 2:
        x = int(input("Informe o valor -> "))
        if arv.remover(x) == False:
            print("Valor não encontrado!")
    elif opcao == 3:
        x = int(input("Informe o valor -> "))
        if arv.buscar(x) != None:
            print("Valor encontrado!")
        else:
            print("Valor não encontrado!")
    elif opcao == 4:
        arv.caminhar()
    elif opcao == 5:
        break



















