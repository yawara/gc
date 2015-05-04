#!/usr/bin/env python3
import random

def comb(n, m, *p):
    if n < m:
      raise Exception("COMB ERROR")
    elif m == 0:
        if n == 0:
            yield p
        else:
            yield from comb(n - 1, m, 0, *p)
    elif n == m:
        yield from comb(n - 1, m - 1, 1, *p)
    else:
        if random.choice((True,False)):
          yield from comb(n - 1, m, 0, *p)
          yield from comb(n - 1, m - 1, 1, *p)
        else:
          yield from comb(n - 1, m - 1, 1, *p)
          yield from comb(n - 1, m, 0, *p)
