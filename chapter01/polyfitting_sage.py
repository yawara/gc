from sage.all import *

from util import create_train_data

# m-degree
m = 5

ws = [var('w' + str(i)) for i in range(m + 1)]

x = var('x')

f = 0

for i in range(m + 1):
    f += ws[i] * x**i
print(f)

for i in range(m + 1):
    print(derivative(f, ws[i]))


def l2_error(f, xs, ts):
    rtv = 0
    for x, t in zip(xs, ts):
        rtv += (f.substitute(x=x) - t)**2
    rtv /= 2
    return rtv

l2e = l2_error(f, *create_train_data(256))

for i in range(m + 1):
    print(derivative(l2e, ws[i]))

solve([derivative(l2e, ws[i]) == 0 for i in range(m + 1)], *ws)
