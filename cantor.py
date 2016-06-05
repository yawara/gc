from math import modf

import numpy as np
import matplotlib.pyplot as plt


# see https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%B3%E3%83%88%E3%83%BC%E3%83%AB%E9%96%A2%E6%95%B0
def cantor(x, N=100):
    if x > 1 or x < 0:
        raise Exception
    if x == 0:
        return 0
    if x == 1:
        return 1

    rtv = 0

    tmp = x
    for i in range(1, N):
        tmp, finteger = modf(tmp * 3)
        r = int(finteger) % 3
        if r == 2:
            rtv += 2**(-i)
        elif r == 1:
            rtv += 2**(-i)
            break

    return rtv


def np_cantor(X):
    Y = np.zeros(len(X))
    for i, x in enumerate(X):
        Y[i] = cantor(x)

    return Y

if __name__ == '__main__':
    X = np.arange(0, 1, 0.001)
    Y = np_cantor(X)

    plt.plot(X, Y)
    plt.show()
    plt.savefig('./cantor.png')
