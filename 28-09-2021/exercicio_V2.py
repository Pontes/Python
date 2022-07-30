from collections import defaultdict

class exercicio:

    def selectionSort(array, size):
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                if array[i] < array[min_idx]:
                    min_idx = i
            (array[step], array[min_idx]) = (array[min_idx], array[step])

    def insertion_sort(array):

        for index in range(1, len(array)):
            currentValue = array[index]
            currentPosition = index

            while currentPosition > 0 and array[currentPosition - 1] > currentValue:
                array[currentPosition] = array[currentPosition -1]
                currentPosition = currentPosition - 1

            array[currentPosition] = currentValue

    def bubble_sort(lista):
        elementos = len(lista) - 1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ordenado = False
                    print(lista)
        return lista

class Grafo(object):

    def __init__(self, arestas, direcionado=False):

        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        return list(self.adj.keys())

    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        self.adj[u].add(v)
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]



class Menu:
    def mPrincicpal(self):
        print("*****************")
        print("*** Bem Vindo ***")
        print("*****************")
        print()
        print("1 - Algoritmos de ordenação")
        print("2 - Grafo")
        op = int(input("Escolha a opção desejada: "))
        if op == 1:
            Menu.mArvore()
        elif op == 2 :
            Menu.mGrafo()
        else:
            print("***********************")
            print("*** Opção Inválida! ***")
            print("*** Tente novamente ***")
            print("***********************")

    def mArvore():
        nElem = int(input(">> Informe a quantidade de elemento que serão digitados: "))
        data = []
        for x in range(nElem):
            if x == 0:
                num = int(input("digite o primeiro número:"))
            else:
                num = int(input("digite o próximo número:"))
            data.append(num)

        size = len(data)
        Menu.mArvoreSub()
        op = int(input(">> Digite uma opção: "))

        if op == 1:
            exercicio.selectionSort(data, size)
            print(data)
        elif op == 2:
            exercicio.insertion_sort(data)
            print(data)
        elif op == 3:
            exercicio.bubble_sort(data)
        else:
            print("Opção Inválida, Por favor digite uma opção válida!")
            Menu.mArvoreSub()

    def mArvoreSub():
        print("****************")
        print("1 - Selection Sort")
        print("2 - Buble Sort")
        print("3 - Insertion Sort")

    def mGrafo():

        print("******************************************")
        nConjGrafo = int(input(">> Informe a quantidade de conjunto de Grafos: "))
        arestas= []

        for x in range(nConjGrafo):
            print("Conjunto Grafo ", x+1)
            n1 = input("Digite o primeiro ponto do grafo: ")
            n2 = input("Digite o segundo ponto do grafo: ")
            n3 = (n1,n2)
            arestas.append(n3)
            print(arestas)

        print("******************************************")
        print("1 - Ver os vertices do Grafo ")
        print("2 - Ver as arestas do Grafo ")
        print("3 - Verificar se o grafo existe ")
        opg = int(input(">> Escolha a Opção desejada: "))

        grafo = Grafo(arestas, direcionado=True)

        if opg == 1:
            print("Vertices: ", grafo.get_vertices())
        elif opg == 2:
            print("Arestas: ", grafo.get_arestas())
        elif opg == 3:
            are1 = input("Digite o primeiro ponto da aresta: ")
            are2 = input("Digite o segundo ponto da aresta: ")
            x = grafo.existe_aresta(are1, are2)
            if x :
                print('O Grafo com os pontos:  ',are1,' e ', are2,' existe!')
            else:
                print(" O Grafo não Existe!")
        else:
            print("Opção Inválida, Por favor digite uma opção válida!")


algor = Menu()
algor.mPrincicpal()

