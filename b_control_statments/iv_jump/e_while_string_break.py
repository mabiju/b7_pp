# demonstrates the use of while loop with break statement.
names = ["Ram", "Sita", "Hari", "Gita","Nita","Mina","Tina","Zina"]
i = 0
while i < len(names):
    """ # dispalys Ram, Sita, Hari, Gita
    print(names[i])
    if names[i] == "Gita":
        break
    i += 1 """
    
    # dispalys Ram, Sita, Hari
    if names[i] == "Gita":
        break
    print(names[i])
    i += 1