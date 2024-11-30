alunos = []

for i in range(5):
    dict = {"matricula": None, "nome": None, "nota1": None, "nota2": None, "nota3": None, "media": None}
    dict["matricula"] = int(input())
    dict["nome"] = input()
    dict["nota1"] = float(input())
    dict["nota2"] = float(input())
    dict["nota3"] = float(input())
    dict["media"] = (dict["nota1"] + dict["nota2"] + dict["nota3"]) / 3
 
    alunos.append(dict)

maior_nota = alunos[0]["nota1"]
indice = 0
for i in range(5):
    if alunos[i]["nota1"] > maior_nota:
        maior_nota = alunos[i]["nota1"]
        indice = i


maior = alunos[0]["media"]
indice_maior = 0
menor = alunos[0]["media"]
indice_menor = 0
for i in range(5):
    if alunos[i]["media"] > maior:
        indice_maior = i
    if alunos[i]["media"] < menor:
        indice_menor = i


nome = alunos[indice]["nome"]
print(f"Aluno {nome} tem a maior nota1: {maior_nota:.2f}")
nome = alunos[indice_maior]["nome"]
media = alunos[indice_maior]["media"]
print(f"Aluno {nome} tem a maior media: {media:.2f}")
nome = alunos[indice_menor]["nome"]
media = alunos[indice_menor]["media"]
print(f"Aluno {nome} tem a menor media: {media:.2f}")

for i in range(5):
    nome = alunos[i]["nome"]
    media = alunos[i]["media"]
    if media >= 7:
        print(f"Aluno {nome} esta aprovado com media {media[i]:.2f}")
    else:
        print(f"Aluno {nome} esta reprovado com media {media[i]:.2f}")
