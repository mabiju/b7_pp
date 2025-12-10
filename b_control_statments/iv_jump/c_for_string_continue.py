# Example of a for loop with a continue statement
names = ["Ram", "Sita", "Hari", "Gita","Nita","Mina","Tina","Zina"]
for name in names:
    # displays except Gita
    if name == "Gita":
        continue
    print(name)
