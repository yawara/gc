from sage.all import *
from util import *
import argparse


def l2_error(f, xs, ts):
    rtv = 0
    for x, t in zip(xs, ts):
        rtv += (f.substitute(x=x) - t)**2
    rtv /= 2
    return rtv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--degree', type=int, default=7)
    parser.add_argument('--n', type=int, default=256)
    args = parser.parse_args()

    n = args.n
    m = args.degree

    x = var('x')
    ws = [var('w' + str(i)) for i in range(m + 1)]

    f = 0
    for i in range(m + 1):
        f += ws[i] * x**i
    print(f)

    l2e = l2_error(f, *create_train_data(n))
    ans = solve([derivative(l2e, ws[i]) == 0 for i in range(m + 1)], *ws)
    f = f.substitute(ans)
    print(f)

    save_plot(lambda arg: f.substitute(x=arg), create_train_data(n))
