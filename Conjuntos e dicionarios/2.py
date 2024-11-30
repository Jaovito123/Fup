list = []
for i in range(5):
    dict = {"model": None, "consume": None}
    dict["model"] = input()
    dict["consume"] = float(input())

    list.append(dict)

economic = list[0]["consume"]
car = 0
for i in range(1, 5):
    if list[i]["consume"] > economic:
        economic = list[i]["consume"]
        car = i

km_per_50l = []
for i in range(5):
    km_per_50l.append(50 * list[i]['consume'])

distance_1k = []
for i in range(5):
    distance_1k.append(1000 / list[i]["consume"])

test = list[car]["model"]
print(f"Carro mais economico: {test}")
for i in range(5):
    temp = list[i]["model"]
    print(f"Carro {temp} percorre {km_per_50l[i]:.2f} kms com 50 litros")
for i in range(5):
    temp = list[i]["model"]
    print(f"Carro {temp} precisa de {distance_1k[i]:.2f} litros para percorrer 1000 kms")