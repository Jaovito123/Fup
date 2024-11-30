vetor = []
vetor.append(int(input()))
menor = vetor[0]
maior = vetor[0]

for i in range(1, 10):
    vetor.append(int(input()))
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print(f"{maior} \n{menor}")
