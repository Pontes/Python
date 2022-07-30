import numpy as np
matriz = np.array([[3,4,1],
                  [3,1,5]])
soma = 0
print("linha, colunas:",matriz.shape)
for i in range(matriz.shape[0]):

    for j in range(matriz.shape[1]):
        soma = soma + int(matriz[i][j])
        print(matriz[i][j])
print('soma é: ', soma)