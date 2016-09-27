import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt


def create_train_data(n):
    x_arr = np.linspace(0, 1, n, endpoint=True)
    t_arr = np.zeros(n)
    for index, x in enumerate(x_arr):
        t_arr[index] = np.sin(2 * np.pi * x) + normal(scale=0.7)

    return (x_arr, t_arr)


def save_plot(func, train_data, filename):
    x = np.linspace(0, 1, 256, endpoint=True)
    t = np.sin(2 * np.pi * x)
    p = list(map(func, x))
    plt.axis([-0.2, 1.2, -3, 3])
    plt.plot(x, t, color='blue', label='sin(2 * pi * x)')
    plt.plot(x, p, color='red', label='prediction')
    x = train_data[0]
    t = train_data[1]
    plt.scatter(x, t)
    plt.legend(loc='upper left')
    plt.savefig(filename)
    plt.clf()
