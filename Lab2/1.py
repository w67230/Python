wiek = int(input("Podaj wiek: "))

if wiek < 4:
    print("Wstep bezplatny")
elif wiek < 19:
    print("Bilet kosztuje 10 zl")
else: print("Bilet kosztuje 20 zl")