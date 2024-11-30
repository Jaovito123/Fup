vetor = []
calculo = []

for i in range(10):
    vetor.append(float(input()))
    print(f"{vetor[i]:.2f}")
for i in range(10):
    calculo.append(vetor[i] ** 2)
    print(f"{calculo[i]:.2f}")
