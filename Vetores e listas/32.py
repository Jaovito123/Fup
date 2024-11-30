vet = []
dc = "S"
cont = 0

while dc == "S" and cont != 5:
    vet.append(input("Aluno: "))
    cont += 1
    if cont < 5:
        dc = input("Deseja inserir novo aluno? [S/N] ").upper()
    if cont == 5 or dc == "N":
        break

name = input("Aluno para pesquisa: ")
for i in range(0, len(vet)):
    if name in vet[i]:
        print(vet[i])
        print(i)
