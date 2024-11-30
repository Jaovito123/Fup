notas = []
soma = 0

for i in range(15):
    notas.append(float(input()))
    soma += notas[i]

media = soma / 15
print(f"{media:.2f}")
