import random

vetor = []
num = int(input())
random.seed(num)
cont = 0
soma = 0

for i in range(12):
    vetor.append(random.uniform(-10, 10))
    if vetor[i] < 0:
        cont += 1
    else:
        soma += vetor[i]
print(cont)
print(f"{soma:.2f}")
