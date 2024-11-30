matriz = []
soma = 0

for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input()))

for i in range(4):
    for j in range(i+1, 4):
        soma += matriz[i][j]

print(soma)