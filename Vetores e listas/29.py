def funcao(vet):
    new_vet = []
    for i in range(len(vet)):
        new_vet.append(vet[i])

    new = []

    while len(new_vet) > 0:
        bigger = new_vet[0]
        for i in range(len(new_vet)):
            if new_vet[i] > bigger:
                bigger = new_vet[i]
        new.append(bigger)
        new_vet.remove(bigger)

    return new
