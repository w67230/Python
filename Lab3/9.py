wysokosc = int(input("Podaj wysokosc choinki"))
s = ""
for i in range(0,wysokosc):
    for x in range(0, i+1):
        s += " *"
    print(s)
    s = ""