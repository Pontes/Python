def heapify(arr, n, i):
    maior = i #inicializar o Maior como raiz
    l = 2 * i + 1
    r = 2 * i + 2

    # verificar se o filho esquerdo da raiz e(and) é
    # maior do que a raiz
    if l < n and arr[i] < arr[l]:
        maior = l

    # verifica se o filho direita da raiz e (and) é
    #
    if r < n and arr[maior] < arr [r]:
        maior = r

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]

        heapify(arr, n, maior)

def heapSort(arr):
    n = len(arr)

    for i in range (n // 2 -1, -1,-1):
        heapify(arr, n, i)

    #extrair os elementos um por um
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12,11,13,5,6,7]
heapSort(arr)
n = len(arr)
print(" a ordenação é: ")
for i in range(n):
    print("%d" %arr[i])


