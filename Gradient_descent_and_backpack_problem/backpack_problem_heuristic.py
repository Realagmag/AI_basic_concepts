import numpy as np
from random import randint

length = 25
m = np.array([randint(1, 20) for _ in range(length)])
p = np.array([randint(1, 20) for _ in range(length)])
M = sum(m) // 2

total_mass = 0
total_value = 0
items_in_backpack = []

n = len(m)
values_with_masses = sorted(list(zip(p, m)), key=lambda x: x[0]/x[1], reverse=True)

for value, mass in values_with_masses:
    if total_mass + mass > M:
        continue
    else:
        total_mass += mass
        total_value += value
        items_in_backpack.append((value, mass))
