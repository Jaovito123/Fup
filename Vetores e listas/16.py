def funcao(vetor):
    new = []

    for i in range(len(vetor)):
        lever = False
        for j in range(len(vetor)):
            if i != j and vetor[i] == vetor[j]:
                lever = True
                break
        if lever == False:
            new.append(vetor[i])
    return new
