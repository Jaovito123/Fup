vetor = []
code = 1
for i in range(100):
    vetor.append(float(input()))

while code != 0:
    code = int(input())
    if code == 1:
        for i in range(len(vetor)):
            print(f"{vetor[i]:.1f}")
    elif code == 2:
        for i in range(99, -1, -1):
            print(f"{vetor[i]:.1f}")
    elif code != 0:
        print("Codigo invalido")
