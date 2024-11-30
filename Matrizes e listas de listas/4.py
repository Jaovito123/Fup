matriz = []

for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input()))

maior = matriz[0][0]

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            l = i
            c = j
        print(matriz[i][j], end=" ")
    print()
print(f"{l} \n{c} \n{maior}")