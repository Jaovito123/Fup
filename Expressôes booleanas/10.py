def funcao(a, b):
    while not b == 0:
        a, b = b, a % b
    return a
