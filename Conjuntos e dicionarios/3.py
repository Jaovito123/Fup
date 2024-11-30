vect = [] 
numb = int(input())

for i in range(numb):
    dict = {"nome": None, "matricula": None, "curso": None}
    dict["nome"] = input()
    dict["matricula"] = int(input())
    dict["curso"] = input()

    vect.append(dict)

for i in range(numb):
    print(vect[i])