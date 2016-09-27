import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt


def create_train_data(n):
    train_data = []
    for i in range(n):
        x = i / (n - 1)
        y = np.sin(2 * np.pi * x) + normal(scale=0.7)
        temp = [x, y]
        train_data.append(temp)

    return train_data


def save_plot(func, train_data, filename):
    x = np.linspace(0, 1, 256, endpoint=True)
    t = np.sin(2 * np.pi * x)
    p = list(map(func, x))
    plt.axis([-0.2, 1.2, -3, 3])
    plt.plot(x, t, color='blue', label='sin(2 * pi * x)')
    plt.plot(x, p, color='red', label='prediction')
    x = [i[0] for i in train_data]
    t = [i[1] for i in train_data]
    plt.scatter(x, t)
    plt.legend(loc='upper left')
    plt.savefig(filename)
    plt.clf()
