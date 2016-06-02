import numpy as np
import matplotlib.pyplot as plt

X =


def contor(x, s=0, t=1):
    if x < s:
        raise Exception
    elif s <= x < s + (t - s) * 1 / 3:
        1 / 2 + contor(x, s, t + (t - s) * 1 / 3)
    elif s + (t - s) * (1 / 3) <= x <= s + (t - s) * (2 / 3):
        return 1 / 2
    elif x > t:
        raise Exception
    elif x < s
