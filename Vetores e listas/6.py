vetor = []
for i in range(8):
    vetor.append(int(input()))
x = int(input())
y = int(input())

soma = vetor[x] + vetor[y]
print(f"{soma:.2f}")