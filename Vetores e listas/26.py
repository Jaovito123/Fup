def funcao(vet_one, vet_two):
    new_vet = []
    for i in range(5):
        if vet_one[i] not in vet_two and vet_one[i] not in new_vet:
            new_vet.append(vet_one[i])
    return new_vet
