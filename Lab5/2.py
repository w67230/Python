

sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for i in sample_dict:
    print(i, sample_dict[i])

list = ["name", "age"]

D = {}
for i in list:
    for x in sample_dict.keys():
        if(i == x):
            D[i] = sample_dict[x]

print(D)

for i in list:
    for x in sample_dict.keys():
        if(i == x):
            del sample_dict[x]
            break
print(sample_dict)

for i in sample_dict.values():
    if(i == "Jones"):
        print("Jones wystepuje w slowniku")
        break
else:
    print("Jones nie wystepuje w slowniku")

sample_dict.pop("city")
sample_dict.setdefault("location", "New york")

print(sample_dict)
