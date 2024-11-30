matriz = []
num = int(input())
cont = num
for i in range(num):
    matriz.append([])
    for j in range(num):
        if cont == num:
            matriz[i].append(1)
            cont = 0
        else:
            matriz[i].append(0)
            cont += 1

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()