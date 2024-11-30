def funcao(x):
    soma = 0
    cont = 0
    for i in range(15):
        soma += x[i]
        if x[i] < 7:
            cont += 1
    media = soma / 15

    variancia = 0
    for i in range(15):
        n = (x[i] - media) ** 2
        variancia += n
    variancia = variancia / 15
    dp = variancia ** 0.5

    return media, dp, cont
