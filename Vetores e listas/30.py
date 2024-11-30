def funcao(vet):
    max_size = len(vet)
    if max_size < 2:
        return -1, -1, -1

    max_tam = 0
    star_1 = -1
    start_2 = -1
    for i in range(2, max_size):
        for j in range(max_size - i + 1):
            segment_1 = vet[j:j+i]

            for k in range(j + 1, max_size - i + 1):
                segment_2 = vet[k:k + i]

                if segment_1 == segment_2 and i > max_tam:
                    max_tam = i
                    star_1 = j
                    start_2 = k
                    break

    if max_tam == 0:
        return -1, -1, -1
    else:
        return star_1, start_2, max_tam
