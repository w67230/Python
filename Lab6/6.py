import math


def pierwiastekDelty(a, b=0, c=0):
    delta = b**2 - 4*a*c
    if(delta >= 0): delta = math.sqrt(delta)
    else: delta = "Liczba ujemna"
    return (delta,)

a = pierwiastekDelty(3, 2, 1)

print(a)