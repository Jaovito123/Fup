matriz = []

for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input()))


for i in range(4):
    for j in range(4):
        print(matriz[j][i], end=" ")
    print()