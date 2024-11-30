vetor = []
soma = 0
for i in range(15):
    vetor.append(int(input()))
    if vetor[i] % 2 == 1:
        soma += vetor[i]

print(soma)
for i in range(15):
    if vetor[i] % 2 == 1:
        print(vetor[i])
