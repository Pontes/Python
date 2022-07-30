class exercicio:

    def menuLista(self):
        print("****************")
        print("***Bem Vindo ***")
        print("****************")
        print()

        data = []
        for x in range(5):
            num = int(input("digite um numero:"))
            data.append(num)

        size = len(data)
        print("****************")
        print("1 - Selection Sort")
        print("2 - Buble Sort")
        print("3 - Insertion Sort")
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
            exercicio.menuLista()

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

exer = exercicio()
exer.menuLista()

