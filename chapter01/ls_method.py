import numpy as np


def ls_method(train_data, dim):
    t = train_data[1]
    t = t.reshape(len(t), 1)
    x = np.empty([len(t), dim + 1], dtype=float)
    for col in range(dim + 1):
        for row, data in enumerate(train_data[0]):
            x[row][col] = data ** col

    trans_x = x.transpose()
    w_vector = np.empty([dim + 1, 1], dtype=float)
    w_vector = np.linalg.inv(trans_x.dot(x)).dot(trans_x.dot(t))

    def f(x):
        y = 0
        for i, w in enumerate(w_vector):
            y += w * (x ** i)
        return y

    return (f, w_vector)
