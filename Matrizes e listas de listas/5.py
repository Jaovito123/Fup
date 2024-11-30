matriz = []
lever = False

for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(input()))

num = int(input())
for i in range(5):
    for j in range(5):
        if matriz[i][j] == num:
            print(i)
            print(j)
            lever = True
            break
    if lever:
        break
if not lever:
    print("Nao encontrado")