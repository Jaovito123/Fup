name = input()
new = ""
vet = []

for i in range(len(name)):
    if name[i].isalpha():
        new += name[i]
for i in range(len(new)):
    lr = new.count(new[i])
    if new[i] not in vet:
        vet.append(new[i])
print(len(vet))
