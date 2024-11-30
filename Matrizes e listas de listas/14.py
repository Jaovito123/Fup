matriz_a = []
matriz_b = []
matriz_c = []

for i in range(4):
    matriz_a.append([])
    for j in range(5):
        matriz_a[i].append(int(input()))

for i in range(4):
    matriz_b.append([])
    for j in range(5):
        matriz_b[i].append(int(input()))

for i in range(4):
    matriz_c.append([])
    for j in range(5):
        matriz_c[i].append(matriz_a[i][j] + matriz_b[i][j])

for i in matriz_c:
    for j in i:
        print(j, end=" ")
    print()