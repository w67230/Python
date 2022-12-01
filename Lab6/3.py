def maks(*liczba):
    a = 0
    for i in liczba:
        if(i > a):
            a = i
    print(a)

maks(4,2,6,1,2,1,1,1)
