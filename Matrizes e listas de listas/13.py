matriz = []

for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input()))

vet = [0, 0, 0, 0, 0]

for i in range(5):
    for j in range(5):
         vet[j] += matriz[i][j]

print(vet)