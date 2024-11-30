matriz = []
num = int(input())

for i in range(num):
    matriz.append([])
    for j in range(num):
        prod = i * j
        matriz[i].append(prod)
for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
