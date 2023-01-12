import numpy as np

tab = np.array(np.zeros((3, 3)))

print(tab)
print()

#pierwszy kwadrat
tab[1:, :2] = 1
print(tab)
tab[:, :] = 0
print()

#drugi kwadrat
tab[:, 2:] = 1
print(tab)
tab[:, :] = 0
print()

#trzeci kwadrat
tab[:2, :] = 1
print(tab)
tab[:, :] = 0
print()

#czwarty kwadrat
tab[:2, :1] = 1
print(tab)
tab[:, :] = 0
print()

#piaty kwadrat
tab[:2, (0,2)] = 1
print(tab)
tab[:, :] = 0
print()