from autograd import value_and_grad
import numpy as np


def gradient_descent(fun, x, beta=0.01, max_iterations=10000, minimal_gradient_value=1e-8, limit_step=False):
    iter = 0
    value_gradient_fun = value_and_grad(fun)   # value_gradient_fun returns value and gradient in x
    current_value, gradient = value_gradient_fun(x)
    x_history = [x]
    y_history = [current_value]

    while iter < max_iterations and np.linalg.norm(gradient) > minimal_gradient_value:
        x_change = beta*gradient
        x = np.clip(x - (np.clip(x_change, -1, 1) if limit_step else x_change), -100, 100)
        current_value, gradient = value_gradient_fun(x)
        x_history.append(x)
        y_history.append(current_value)
        iter += 1

    return x_history, y_history
