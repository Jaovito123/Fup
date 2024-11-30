vet = []
while len(vet) < 12:
    num = int(input())
    if num not in vet:
        vet.append(num)
    else:
        print(f"Numero {num} ja existe, escreva outro")
print(vet)
