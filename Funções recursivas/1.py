# Crie uma função recursiva que receba um número inteiro positivo n e calcule o 
# somatório dos números de 1 até n.

def funcao(n): 
    if n > 0:
        return funcao(n - 1)
    else:
        return 1
print(funcao(4))