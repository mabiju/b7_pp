# displays Ram, Sita, Hari
names = ["Ram", "Sita", "Hari", "Gita","Nita","Mina","Tina","Zina"]
i = 0
while i < len(names):
    # skips Gita
    if names[i] == "Gita":
        i+=1
        continue
    print(names[i])
    i += 1
    