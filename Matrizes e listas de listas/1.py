matriz = []
cont = 0
for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input()))
        if matriz[i][j] > 10:
            cont += 1
print(cont) 