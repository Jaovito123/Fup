def funcao(vetor, x):
    new = []
    for i in range(len(vetor)):
        if vetor[i] % x == 0:
            new.append(vetor[i])
    return new
