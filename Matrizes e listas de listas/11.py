matriz = []
soma = 0

for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input()))

v1 = 0
v2 = 3

for i in range(4):
    soma += matriz[v1][v2]
    v1 += 1
    v2 -= 1
print(soma) 