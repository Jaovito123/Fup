vetor = []
stop = 0
num = 1

while stop == 0:
    if num % 7 != 0 and num % 10 != 7:
        vetor.append(num)
    if len(vetor) == 100:
        stop = 1
    num += 1
print(vetor)
