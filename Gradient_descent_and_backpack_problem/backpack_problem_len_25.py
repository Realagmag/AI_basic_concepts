import numpy as np
from itertools import product
from random import randint

length = 25

m = np.array([randint(1, 20) for _ in range(length)])
p = np.array([randint(1, 20) for _ in range(length)])
M = sum(m) // 2

n = len(m)
combination_matrix = np.array(list(product([0, 1], repeat=n)))

values = combination_matrix@p
masses = combination_matrix@m

highest_value = 0
best_combination = None
for i in range(len(values)):
    if masses[i] <= M and values[i] > highest_value:
        highest_value = values[i]
        best_combination = combination_matrix[i]

