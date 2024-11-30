vetor = []
cont = 0
for i in range(15):
    vetor.append(int(input()))
    if vetor[i] % 2 == 0:
        cont += 1
print(cont)
for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print(vetor[i])
