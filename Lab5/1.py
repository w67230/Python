values = [10, 20, 30]

keys = ["ten", "twenty", 'thirty']

D = dict(zip(keys, values))
Di = {}

for i in range(len(keys)):
    Di[keys[i]] = values[i]

print(Di, " - for")
print(D, " - zip")

Ddrugi = dict(thirty = 30, forty = 40, fifty = 50)

zlaczone = {}
zlaczone.update(D)
zlaczone.update(Ddrugi)

print(zlaczone)