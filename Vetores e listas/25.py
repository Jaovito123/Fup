def funcao(vet_one, vet_two):
    new_vet = []
    for i in range(len(vet_one)):
        if vet_one[i] not in new_vet:
            new_vet.append(vet_one[i])

    for i in range(len(vet_two)):
        if vet_two[i] not in new_vet:
            new_vet.append(vet_two[i])

    return new_vet
