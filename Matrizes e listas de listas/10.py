"""
Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão na diagonal principal. 
Use apenas um comando de repetição. Não use comandos nem funções do python ou de suas 
bibliotecas que já façam isso.
"""

matriz = []
soma = 0

for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(int(input()))

for i in range(4):
    soma += matriz[i][i]

print(soma)