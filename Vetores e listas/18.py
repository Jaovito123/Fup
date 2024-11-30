def funcao(vet_a, vet_b):
    vet_c = []
    index = 0
    while len(vet_c) < 5:
        vet_c.append(vet_a[index] - vet_b[index])
        index += 1
    return vet_c
