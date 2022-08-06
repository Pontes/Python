import numpy as np

matriz = np.array([[2,3,1],
                   [4,5,7]])

print(matriz)
print(matriz.shape)
print(matriz[0],"primeiro linha da matriz")
print(matriz[1],"segunda linha da matriz")
print(matriz[0][1])
print(matriz[1][2])

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])


# agenda = np.array([['Pontes Junior', "21999-470-170","vivo"],
#                 ["Emanuelle", "2199798748765","vivo"]])
# print(agenda[0][0]," - ",agenda[0][1])
