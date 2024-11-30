matriz = []
matriz_numero_divididos = []

def primo(numero):
    if numero == 0:
        return False
    if numero == 2:
        return True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
        
    return True

for linha in range(12):
    matriz.append([])
    matriz_numero_divididos.append([])
    for coluna in range(13):
        numero = int(input(''))
        matriz[linha].append(numero)

for coluna in range(13):
    maior_numero_primo = float('-inf')
    menor_numero = float('inf')
    for linha in range(12):
        if primo(abs(matriz[linha][coluna])) and matriz[linha][coluna] > maior_numero_primo:
            maior_numero_primo = matriz[linha][coluna]
        if matriz[linha][coluna] < menor_numero:
            menor_numero = matriz[linha][coluna]

    if maior_numero_primo != float('-inf'):
        divisor = maior_numero_primo
    else:
        divisor = menor_numero
    
    for linha in range(12):
        matriz_numero_divididos[linha].append(matriz[linha][coluna] / divisor)

for item in matriz:
    for numero in item:
        print(f'{numero:.2f}', end=' ')
    print()

print()

for item in matriz_numero_divididos:
    for numero in item:
        print(f'{numero:.2f}', end=' ')
    print()