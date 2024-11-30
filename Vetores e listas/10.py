vetor = []

for i in range(20):
    vetor.append(int(input()))
    if vetor[i] < 0:
        print(0)
    else:
        print(vetor[i])
