matriz = []
for i in range(10):
    matriz.append([])
    for j in range(10):
        if i < j:
            matriz[i].append(2 * i + 7 * j - 2)
        elif i == j:
            matriz[i].append(3 * i ** 2 - 1)
        else:
            matriz[i].append(4 * i ** 3 - 5 * j ** 2 + 1)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()