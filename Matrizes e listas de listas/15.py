matriz_1 = []
matriz_2 = []
matriz_produto = []

for linha in range(5):
    matriz_1.append([])
    for coluna in range(5):
        matriz_1[linha].append(int(input('')))

for linha in range(5):
    matriz_2.append([])
    for coluna in range(5):
        matriz_2[linha].append(int(input('')))
    
for item in range(5):
    matriz_produto.append([])
    for linha in range(5):
        soma = 0
        for coluna in range(5):
          soma += matriz_1[item][coluna] * matriz_2[coluna][linha]
        matriz_produto[item].append(soma)

for item in matriz_produto:
    for numero in item:
        print(numero, end=' ')
    print()