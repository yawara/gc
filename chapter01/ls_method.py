import numpy as np


def ls_method(train_data, dim):
    t = [i[1] for i in train_data]
    t = np.array(t)
    data_count = len(train_data)
    t = t.reshape(data_count, 1)
    x = np.empty([data_count, dim + 1], dtype=float)
    for col in range(dim + 1):
        for row, data in enumerate(train_data):
            x[row][col] = data[0] ** col

    trans_x = x.transpose()
    w_vector = np.empty([dim + 1, 1], dtype=float)
    w_vector = np.linalg.inv(trans_x.dot(x)).dot(trans_x.dot(t))

    def f(x):
        y = 0
        for i, w in enumerate(w_vector):
            y += w * (x ** i)
        return y

    return (f, w_vector)
