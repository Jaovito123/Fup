vet = []
for i in range(10):
    vet.append(int(input()))
    cont = 0
    if vet[i] > 0:
        for j in range(1, vet[i]+1):
            if vet[i] % j == 0:
                cont += 1
    else:
        for j in range(vet[i], 0):
            if vet[i] % j == 0:
                cont += 1
    if cont == 2:
        print(vet[i])
        print(i)
