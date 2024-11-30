matriz = []
matriz_numero_abs = []
maior_numero_abs = 0

for linha in range(12):
    matriz.append([])
    for coluna in range(13):
        matriz[linha].append(int(input('')))

for linha in range(12):
    maior_numero_abs = 0
    matriz_numero_abs.append([])

    for coluna in range(13):
        modulo_do_numero = abs(matriz[linha][coluna])
        if coluna == 0:
            maior_numero_abs = modulo_do_numero

        elif modulo_do_numero > maior_numero_abs:
            maior_numero_abs = modulo_do_numero
   
    for coluna in range(13):
        matriz_numero_abs[linha].append(matriz[linha][coluna]/maior_numero_abs)

for item in matriz:
    for numero in item:
        print(f'{numero:.2f}', end=' ')
    print()

print()

for item in matriz_numero_abs:
    for numero in item:
        print(f'{numero:.2f}', end=' ')
    print()