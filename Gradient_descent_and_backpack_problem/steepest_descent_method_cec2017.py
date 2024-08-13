from cec2017.functions import f1, f2, f3
import numpy as np
import matplotlib.pyplot as plt
from gradient_descent import gradient_descent


MAX_X = 100
PLOT_STEP = 0.1
UPPER_BOUND = 100
DIMENSIONALITY = 10
x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)
x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
X, Y = np.meshgrid(x_arr, y_arr)
Z = np.empty(X.shape)
q = f1        # Change to f2 or f3 to use on different functions
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = q(np.array([X[i, j], Y[i, j]]))

plt.contour(X, Y, Z, 20)

x_history, y_history = gradient_descent(q, x, beta=1e-8, max_iterations=1000, limit_step=False)
for i in range(len(x_history)-1):
    dx1 = x_history[i+1][0]-x_history[i][0]
    dx2 = x_history[i+1][1]-x_history[i][1]
    plt.arrow(x_history[i][0], x_history[i][1], dx1, dx2, head_width=0.5, head_length=0.5, fc='k', ec='k')
print(y_history[-1])
plt.show()
