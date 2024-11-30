vetor = []
for i in range(10):
    vetor.append(int(input()))

for i in range(10):
    for j in range(i + 1, len(vetor)):
        if vetor[i] == vetor[j]:
            print(vetor[i])
